import os, logging, datetime
from os.path import join, dirname

from dotenv import load_dotenv
import grpc

import protos.yysystem.audioclassification_pb2 as audioclassification_pb2
import protos.yysystem.audioclassification_pb2_grpc as audioclassification_pb2_grpc

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

ENDPOINT_ID = os.environ.get("ENDPOINT_ID")

SAMPLE_RATE_HERTZ = int(os.environ.get("SAMPLE_RATE_HERTZ"))
CHUNK = SAMPLE_RATE_HERTZ // 10


def send_config_before_audio_classification(generator, replacement):
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
            with MicStreamInput(rate=SAMPLE_RATE_HERTZ, channel=1, dtype="int16", chunk=CHUNK) as stream:
                logger.info("Start")
                audio_generator = stream.generator()
                stub = audioclassification_pb2_grpc.YYAudioClassificationStub(channel)
                streaming_config=audioclassification_pb2.StreamingConfig(
                    custom_config=audioclassification_pb2.Config(top_n=2),
                    default_config=audioclassification_pb2.Config(top_n=5),
                    use_default_results=True,
                    endpoint_id=ENDPOINT_ID,
                )
                entry_request = audioclassification_pb2.ClassifyStreamRequest(streaming_config=streaming_config)

                requests = send_config_before_audio_classification((audioclassification_pb2.ClassifyStreamRequest(audiobytes=audio_data.tobytes()) for audio_data in audio_generator), entry_request)
                responses = stub.ClassifyStream(
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
