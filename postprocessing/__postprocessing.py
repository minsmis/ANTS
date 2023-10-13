from abc import *
import core.antstimeseries as timeseries


class Postprocessing(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Postprocessing, self).__init__()

    @classmethod
    def to_freq_power(cls, waves):
        pass

    @classmethod
    def to_time_power(cls, waves):
        pass

    @classmethod
    def stack_power(cls, ants):
        pass

    @classmethod
    def sem(cls, stack):
        pass

    @classmethod
    def ts_to_sec(cls, timestamps, sample_frequency):
        pass
