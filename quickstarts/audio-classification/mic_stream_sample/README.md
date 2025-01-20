# YYAPIs Audio_classification Python サンプル コンソールアプリ

## 事前準備

- [git] (https://git-scm.com/downloads) - ソースコード管理システム
- [<u>開発者コンソール</u>](https://api-web.yysystem2021.com) の `audioclassification.proto`、 `API キー`、`エンドポイントID`
- [サンプルデータのデプロイ] (https://github.com/YYSystem/yyapis-docs/wiki/ClassifyStream) - サンプルデータのデプロイまで終わらせてください。
- [python] (https://www.python.org/downloads/) (推奨バージョン 3.13.1) - 自身の好みの仮想環境を使いたい方や python だけインストールしたい方は python と pip が使えるようにしてください。

## サンプルコードのダウンロード

1. git を使用して、任意のディレクトリにサンプルコードをダウンロードします。

```bash
git clone https://github.com/YYSystem/yyapis-python.git
```

2. clone したプロジェクトのディレクトリを移動します。

```bash
cd yyapis-python/quickstarts/audio-classification/mic_stream_sample
```

3. `mic-stream-sample` の直下に `protos` を作成します。
```bash
mkdir protos
```

4. YYAPIs 開発者コンソールから音響分類 API の proto ファイル(`audioclassification.proto`)をダウンロードして、 `protos` ディレクトリを配置します。

```bash
yyapis-node/quickstarts/speech-to-text/mic-stream-sample/protos/audioclassfication.proto # ← ここに配置する
```

## API キー　の設定

1. mic-stream-sample の直下に .envファイルを作成します。

```bash
touch .env
```

2. 以下のソースコードをコピーして .env ファイルに貼り付けます。

```.env
# grpc settings
API_KEY=YOUR API KEY
API_ENDPOINT=api-grpc-2.yysystem2021.com
API_PORT=443
ENDPOINT_ID=YOUR ENDPOINT ID

# streamingConfig
MODEL=10
ENCODING=LINEAR16
LANGUAGE_CODE=4
SAMPLE_RATE_HERTZ=16000
ENABLE_INTERIM_RESULTS=true
AUDIO_CHANNEL_COUNT=1
```

YOUR API KEY と YOUR ENDPOINT ID に、開発者コンソールから取得した値を貼り付けてください。

## [任意] Rye のインストール

1. curl コマンドを実行して Rye をインストールします。

```bash
curl -sSf https://rye.astral.sh/get | bash
```

2. Rye のパスを通します。

```bash
echo 'source "$HOME/.rye/env"' >> ~/.profile
```

## [任意] Rye で仮想環境を構築する

1. プロジェクトのディレクトリまで移動します。

```bash
cd
cd yyapis-python/quickstarts/audio-classification
```

2. プロジェクトのディレクトリで Rye での仮想環境を立ち上げます。

```bash
rye init
```

3. python のバージョンを指定してインストールします。

```bash
rye pin 3.13
rye sync
```

4. 仮想環境をアクティベートします。

```bash
source .venv/bin/activate
```

5. ライブラリをインストールします。

```bash
cd mic_stream_sample
rye add $(cat requirements.txt)
rye sync
```

[他の仮想環境や Python と pip のみインストールした場合]
```bash
pip install -r requirements.txt
```

## サンプルアプリの実行

```bash
python codegen.py
python main.py
```