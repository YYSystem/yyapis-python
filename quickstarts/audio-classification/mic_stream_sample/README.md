# YYAPIs Speech-to-Text

Python サンプル コンソールアプリ

## 準備

Python 3.10.6をインストールしてください

**protoファイルの設定**

\[[<u>開発者コンソール</u>](https://api-web.yysystem2021.com)\]から最新の
**yysystem.audioclassification.proto** ファイルをダウンロードして、**protos/**
ディレクトリに配置します。

**フォルダの構造**

```
./ # ソリューションフォルダ
  protos/
    yysystem.audioclassification.proto # ここに配置する
    …
  …
```

**.envファイルの作成**

quickstarts/audio-classification/mic_stream_sample ディレクトリに次の**.envファイル**を作成します

**.env**

```
# grpc settings
API_KEY=<your_key>
API_ENDPOINT=api-grpc-2.yysystem2021.com
API_PORT=443

# streamingConfig
SAMPLE_RATE_HERTZ=16000
ENDPOINT_ID=<your_endpont_id>
```

**your_key** の値を開発者コンソールで発行した Speech-to-Text の API
キーに置き換えます。

**your_endpoint_id** の値を開発者コンソールでトレーニング、デプロイしたデプロイIDに置き換えます。

## ビルドと実行

**bash**

```
$ pip install -r requirements.txt
$ python codegen.py
$ python main.py
```
