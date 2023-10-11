from abc import *
import core.antstimeseries as timeseries


class Preprocessing(timeseries.TimeSeries, metaclass=ABCMeta):

    def downsampling(self, target_fs):
        pass

    def normalization(self, method):
        pass

    def bandpass_butter(self, target_band):
        pass
