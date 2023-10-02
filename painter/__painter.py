from abc import *
import core.coretimeseries as timeseries


class Painter(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Painter, self).__init__()

    def powerSpectrum(self, directory):
        pass
