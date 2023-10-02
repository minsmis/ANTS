from abc import *
import core.antstimeseries as timeseries


class Postprocessing(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Postprocessing, self).__init__()

    @classmethod
    def toFreqPower(cls, waves):
        pass

    @classmethod
    def toTimePower(cls, waves):
        pass

    @classmethod
    def stackPower(cls, ants):
        pass

    @classmethod
    def sem(cls, stack):
        pass
