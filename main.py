import time
import json
from web3 import Web3

with open('config.json') as f:
   config = json.load(f)

infura_url = config['infura_url']
contract_address = config['contract_address']
contract_abi = config['contract_abi']
account_address = config['account_address']
private_key = config['private_key']
mint_amount = config['mint_amount']

w3 = Web3(Web3.HTTPProvider(infura_url))
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

mint_amount_wei = mint_amount * 10**8
mint_amount_hex = w3.to_hex(mint_amount_wei)
mint_amount_padded = mint_amount_hex[2:].zfill(64)
mint_signature = '0xa0712d68'

nonce = w3.eth.get_transaction_count(account_address)

def get_dynamic_gas_price():
   gas_price = w3.eth.gas_price
   gas_price_multiplier = 3.5
   dynamic_gas_price = int(gas_price * gas_price_multiplier)
   return dynamic_gas_price

def call_mint_function():
   global nonce
   try:
       dynamic_gas_price = get_dynamic_gas_price()
       print(f"\033[94mCalling mint function with nonce: {nonce}\033[0m")
       transaction = contract.functions.mint(mint_amount_wei).build_transaction({
           'from': account_address,
           'gas': 500000,
           'gasPrice': dynamic_gas_price,
           'nonce': nonce,
       })
       signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
       transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
       print(f"\033[92mTransaction sent. Hash: {transaction_hash.hex()}\033[0m")
       transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
       print(f"Transaction successful. Receipt: {transaction_receipt}")
       nonce += 1
   except Exception as e:
       print(f"Transaction failed. Error: {e}")
       nonce = w3.eth.get_transaction_count(account_address)

while True:
   call_mint_function()
   time.sleep(5)
