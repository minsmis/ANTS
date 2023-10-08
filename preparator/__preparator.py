from abc import *
import core.antstimeseries as timeseries


class Preparator(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Preparator, self).__init__()

    @classmethod
    def getSubdirectory(self, superior_path):
        pass