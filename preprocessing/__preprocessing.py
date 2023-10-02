from abc import *
import core.antstimeseries as timeseries


class Preprocessing(timeseries.TimeSeries, metaclass=ABCMeta):

    def downsampling(self, target_fs):
        pass

    def normalization(self, method):
        pass

    def bandpassButter(self, target_band):
        pass
