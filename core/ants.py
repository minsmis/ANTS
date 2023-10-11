import preparator.dirprep as dirprep
import extractor.caller as caller
import preprocessing.downsampling as downsampling
import preprocessing.filters as filters
import preprocessing.normalization as normalization
import timefrequency.wavelet as wavelet
import timefrequency.multitaper as multitaper
import postprocessing.power as post_power
import painter.plots as plots
import circulus.statistics as circular_stat
import numpy as np


# User interface
class Ants(caller.CallTimeSeries, downsampling.Downsampling, dirprep.DirPrep,
           filters.Filters, normalization.Normalization, wavelet.Wavelet, multitaper.Multitaper,
           post_power.Power, plots.Plots, circular_stat.Statistics):

    def __init__(self):
        super(Ants, self).__init__()

    @classmethod
    def batch(cls, batch_size):
        batch_ants = np.array([Ants() for i in np.arange(0, batch_size)])
        return batch_ants
