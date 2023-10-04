from abc import *
import core.antstimeseries as timeseries


class TimeFrequency(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(TimeFrequency, self).__init__()

    def waveletTransform(self, **kwargs):
        pass

    def multitapers(self, **kwargs):
        pass

    def spectrogram(self, **kwargs):
        pass
