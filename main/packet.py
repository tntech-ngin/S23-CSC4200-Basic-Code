import struct


class Packet:
    def __init__(self, data=0, formatter='!I'):
        self._data = data
        self._formatter = formatter

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def formatter(self):
        return self._formatter

    @formatter.setter
    def formatter(self, value):
        self._formatter = value

    def pack(self):
        return struct.pack(self.formatter, self.data)