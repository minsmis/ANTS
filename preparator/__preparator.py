from abc import *
import core.antstimeseries as timeseries


class Preparator(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Preparator, self).__init__()

    @classmethod
    def get_subdirectory(self, superior_path):
        pass

    @classmethod
    def get_data_directory(cls, superior_path, **kwargs):
        pass

    @classmethod
    def get_spikes(cls, superior_path, expander='txt', **kwargs):
        pass
