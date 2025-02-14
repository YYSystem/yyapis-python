# YYAPIs speech-to-text Python サンプル コンソールアプリ

## 事前準備

- [<u>git</u>](https://git-scm.com/downloads) - ソースコード管理システム
- [<u>開発者コンソール</u>](https://api-web.yysystem2021.com) の `yysystem.proto`、 `API キー`
- [<u>python</u>](https://www.python.org/downloads/) (推奨バージョン 3.13.1) - 自身の好みの仮想環境を使いたい方や python だけインストールしたい方は python と pip が使えるようにしてください。

## サンプルコードのダウンロード

1. git を使用して、任意のディレクトリにサンプルコードをダウンロードします。

```bash
git clone https://github.com/YYSystem/yyapis-python.git
```

2. clone したプロジェクトのディレクトリを移動します。

```bash
cd yyapis-python/quickstarts/speech-to-text/mic_stream_sample
```

3. `mic-stream-sample` の直下に `protos` を作成します。
```bash
mkdir protos
```

4. YYAPIs 開発者コンソールから音声認識 API の proto ファイル(`yysystem.proto`)をダウンロードして、 `protos` ディレクトリを配置します。

```bash
yyapis-python/quickstarts/speech-to-text/mic-stream-sample/protos/yysystem.proto # ← ここに配置する
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
# streamingConfig
MODEL=10
ENCODING=LINEAR16
LANGUAGE_CODE=4
SAMPLE_RATE_HERTZ=16000
ENABLE_INTERIM_RESULTS=true
AUDIO_CHANNEL_COUNT=1
```

YOUR API KEY に、開発者コンソールから取得した値を貼り付けてください。

## [任意] uv のインストール

1. curl コマンドを実行して uv をインストールします。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. shellを再起動して、バージョンを確認します。

```bash
uv --version
```

## [任意] uv で仮想環境を構築する

1. プロジェクトのディレクトリまで移動します。

```bash
cd
cd yyapis-python/quickstarts/speech-to-text
```

2. プロジェクトのディレクトリで uv での仮想環境を立ち上げます。

```bash
uv init
uv sync
```

3. python のバージョンを指定してインストールします。

```bash
uv python pin 3.13
uv sync
```

4. 仮想環境をアクティベートします。

```bash
. .venv/bin/activate
```

5. ライブラリをインストールします。

```bash
cd mic_stream_sample
uv add -r requirements.txt
uv sync
```

[他の仮想環境や Python と pip のみインストールした場合]
```bash
pip install -r requirements.txt
```

## サンプルアプリの実行

```bash
uv run codegen.py
uv run main.py
```