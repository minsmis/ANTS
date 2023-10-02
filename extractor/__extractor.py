from abc import *
import core.antstimeseries as timeseries


class Extractor(timeseries.TimeSeries, metaclass=ABCMeta):
    @classmethod
    def callAllFolders(cls, dir):
        pass

    def callNeuralynx(self, dir_file):
        pass
