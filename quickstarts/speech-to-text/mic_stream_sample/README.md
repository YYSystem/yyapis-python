# YYAPIs Speech-to-Text

Python サンプル コンソールアプリ

## 準備

Python 3.10.6をインストールしてください

**protoファイルの設定**

\[[<u>開発者コンソール</u>](https://api-web.yysystem2021.com)\]から最新の
**yysystem.proto** ファイルをダウンロードして、**pyshon/protos/**
ディレクトリに配置します。

**フォルダの構造**

```
python/ # ソリューションフォルダ
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
API_KEY=<your_key>;
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
