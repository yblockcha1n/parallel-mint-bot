# ParallelTestnet Token Minting Bot

![image](https://github.com/yblockcha1n/parallel-mint-bot/assets/144770048/00f9e4cf-6bd5-4f66-91be-ae5510c9649b)


## 概要

弊BOTは Parallel Testnetでのエアドロップ目的でトークンをミントするために作成されました。

ただ、既にテストネットは終了しているため現時点では何の効力もないです。

## 必要条件

- Python 3.11
- Web3.py ライブラリ

## セットアップ

1. 必要なライブラリをインストールします：`pip install web3`

**注**: インストール時に crypto 関連のエラーが発生した場合は、以下のコマンドで pycryptodome もインストールしてください：

`pip install pycryptodome`

2. `config.json` ファイルを編集し、以下の情報を入力します：
- `INFURA_ID`
- `PRIVATE-KEY`

**セキュリティに関する注意**: セキュリティを強化したい場合は、設定情報を `config.json` ではなく、`.env` ファイルや環境変数に保存することをお勧めします。

## 使用方法

セットアップが完了したら、以下のコマンドで実行します：`python main.py`
