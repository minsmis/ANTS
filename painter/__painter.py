from abc import *
import core.antstimeseries as timeseries


class Painter(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Painter, self).__init__()

    def power_spectrum(self, **kwargs):
        pass
