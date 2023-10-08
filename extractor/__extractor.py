from abc import *
import core.antstimeseries as timeseries


class Extractor(timeseries.TimeSeries, metaclass=ABCMeta):

    def callNeuralynx(self, dir_file):
        pass
