# YYAPIs Speech-to-Text

Python サンプル コンソールアプリ

## 事前準備

- [git](https://git-scm.com/downloads) - ソースコード管理システム
- [Miniconda](https://docs.anaconda.com/miniconda/) (Python 3.12.2) - パッケージ管理ツール conda と Python 基本パッケージを内包するディストリビューション
- [<u>開発者コンソール</u>](https://api-web.yysystem2021.com) の `yysystem.proto` のダウンロード、`API キー` の取得

**protoファイルの設定**

**yysystem.proto** ファイルを **mic_stream_sample/protos/**
ディレクトリに配置します。

**フォルダの構造**

```
mic_stream_sample/ # ソリューションフォルダ
  protos/
    yysystem.proto # ここに配置する
    …
  …
```

**.envファイルの作成**

python/ ディレクトリに次の**.envファイル**を作成します

**.env**

```
# grpc settings
API_KEY=<your_key>
API_ENDPOINT=api-grpc-2.yysystem2021.com
API_PORT=443

# streamingConfig
MODEL=10
ENCODING=LINEAR16
LANGUAGE_CODE=4
SAMPLE_RATE_HERTZ=16000
ENABLE_INTERIM_RESULTS=true
AUDIO_CHANNEL_COUNT=1
```

**YOUR_API_KEY** の値を開発者コンソールで発行した Speech-to-Text の API
キーに置き換えます。

## ビルドと実行

**bash**

```
$ pip install -r requirements.txt
$ python codegen.py
$ python main.py
```
