import queue

import numpy as np
import sounddevice as sd


class MicStreamInput(object):
    def __init__(
        self, rate, chunk, input_device_id=None, dtype="int16", channel=1
    ):
        self._rate = rate
        self._chunk = chunk
        self._channel = channel

        self._buff = queue.Queue()
        self.closed = True
        self.stream = sd.InputStream(
            samplerate=self._rate,
            channels=self._channel,
            device=input_device_id,
            dtype=dtype,
            callback=self._callback,
            blocksize=self._chunk,
        )

    def __enter__(self):
        self.stream.start()
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        self.stream.close()
        self.closed = True
        self._buff.put(None)

    @staticmethod
    def get_devices():
        return sd.query_devices()

    def set_device(self, input_device_id, output_device_id):
        sd.default.device = [input_device_id, output_device_id]

    def _callback(self, indata, frames, time, status):
        self._buff.put(indata.copy())

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = chunk
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data = np.concatenate([data, chunk])
                except queue.Empty:
                    break
            yield data
