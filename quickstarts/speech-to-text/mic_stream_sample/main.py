import os, logging, datetime
from os.path import join, dirname
import json

from dotenv import load_dotenv
import grpc

import protos.yysystem_pb2 as yysystem_pb2
import protos.yysystem_pb2_grpc as yysystem_pb2_grpc
from microphone import MicStreamInput


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


format = "%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s"

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(format))

dt_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

logger = logging.getLogger("MAIN_LOG")
logger.setLevel(logging.INFO)

logger.addHandler(stream_handler)


API_KEY = os.environ.get("API_KEY")
API_ENDPOINT = os.environ.get("API_ENDPOINT")
API_PORT = os.environ.get("API_PORT")


MODEL = int(os.environ.get("MODEL"))
ENCODING = os.environ.get("ENCODING")
LANGUAGE_CODE = int(os.environ.get("LANGUAGE_CODE"))
SAMPLE_RATE_HERTZ = int(os.environ.get("SAMPLE_RATE_HERTZ"))
ENABLE_INTERIM_RESULTS = bool(os.environ.get("ENABLE_INTERIM_RESULTS"))
ENABLE_WORD = bool(os.environ.get("ENABLE_WORD"))
AUDIO_CHANNEL_COUNT = int(os.environ.get("AUDIO_CHANNEL_COUNT"))

CHUNK = SAMPLE_RATE_HERTZ // 10

streaming_config_dict = {
    "encoding": ENCODING,
    "sample_rate_hertz": SAMPLE_RATE_HERTZ,
    "language_code": LANGUAGE_CODE,
    "enable_word": bool(ENABLE_WORD),
    "model": MODEL,
    "enable_interim_results": bool(ENABLE_INTERIM_RESULTS),
    "translate_to": [],
    "audio_channel_count": AUDIO_CHANNEL_COUNT
}

def send_config_before_speech_recognition(generator, replacement):
    replaced = False
    for item in generator:
        if not replaced:
            yield replacement
            replaced = True
        else:
            yield item

def run():
    try:
        with grpc.secure_channel(f"{API_ENDPOINT}:{API_PORT}", grpc.ssl_channel_credentials()) as channel:
            with MicStreamInput(rate=SAMPLE_RATE_HERTZ, chunk=CHUNK) as stream:
                logger.info("Start")
                audio_generator = stream.generator()
                stub = yysystem_pb2_grpc.YYSpeechStub(channel)
                streaming_config = yysystem_pb2.StreamRequest(streaming_config=yysystem_pb2.StreamingConfig(**streaming_config_dict))

                requests = send_config_before_speech_recognition((yysystem_pb2.StreamRequest(audiobytes=audio_data.tobytes()) for audio_data in audio_generator), streaming_config)
                responses = stub.RecognizeStream(
                    requests,
                    metadata=[
                        ("x-api-key", API_KEY)
                    ]
                )
                for response in responses:
                    logger.info(response)
    
    except grpc.RpcError as e:
        import traceback
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    run()
