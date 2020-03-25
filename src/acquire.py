import pyaudio


class AudioAcquire(object):

    CHUNK = 1024 * 50
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    def __init__(self):

        self.pause = False

        # stream object
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=False,
            frames_per_buffer=self.CHUNK,
        )

    def read(self):
        data = self.stream.read(self.CHUNK)
        print(data)
        return data
