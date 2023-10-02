import extractor.caller as caller
import preprocessing.downsampling as downsampling
import preprocessing.filters as filters
import preprocessing.normalization as normalization
import timefrequency.wavelet as wavelet
import postprocessing.power as post_power
import painter.plots as plots
import numpy as np


# User interface
class Ants(caller.CallTimeSeries, downsampling.Downsampling,
           filters.Filters, normalization.Normalization, wavelet.Wavelet,
           post_power.Power, plots.Plots):

    def __init__(self):
        super(Ants, self).__init__()

    @classmethod
    def batch(cls, batch_size):
        batch_ants = np.array([Ants() for i in np.arange(0, batch_size)])
        return batch_ants
