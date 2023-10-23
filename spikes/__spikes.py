from abc import *
import core.antstimeseries as timeseries


class Spikes(timeseries.TimeSeries, metaclass=ABCMeta):
    def __init__(self):
        super(Spikes, self).__init__()

    @classmethod
    def classify(cls, spk_s, mode):
        pass

    @classmethod
    def calc_cv2(cls, spk_s):
        pass

    @classmethod
    def mad(cls, data):
        pass

    @classmethod
    def calc_mad(cls, spk_s):
        pass
