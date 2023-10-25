from abc import *
import core.antstimeseries as timeseries


class Extractor(timeseries.TimeSeries, metaclass=ABCMeta):

    def call_neuralynx(self, path):
        pass

    def call_nlx_events(self, path):
        pass