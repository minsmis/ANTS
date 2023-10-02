from abc import *
import core.antstimeseries as timeseries


class TimeFrequency(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(TimeFrequency, self).__init__()

    def waveletTransform(self):
        pass

    @classmethod
    def toFPower(self, waves):
        pass

    @classmethod
    def toTPower(self, waves):
        pass
