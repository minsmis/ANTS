from abc import *
import core.coretimeseries as timeseries


class Extractor(timeseries.TimeSeries, metaclass=ABCMeta):
    @classmethod
    def callAllFolders(cls, dir):
        pass

    def callNeuralynx(self, dir_file):
        pass
