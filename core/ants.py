import preparator.dirprep as dirprep
import extractor.caller as caller
import preprocessing.downsampling as downsampling
import preprocessing.filters as filters
import preprocessing.normalization as normalization
import timefrequency.wavelet as wavelet
import timefrequency.multitaper as multitaper
import postprocessing.power as post_power
import postprocessing.scale as scale
import painter.plots as plots
import circulus.statistics as circular_stat

import os
import datetime
import pickle
import numpy as np


# User interface
class Ants(caller.CallTimeSeries, downsampling.Downsampling, dirprep.DirPrep,
           filters.Filters, normalization.Normalization, wavelet.Wavelet, multitaper.Multitaper,
           post_power.Power, scale.Scale, plots.Plots, circular_stat.Statistics):

    def __init__(self):
        super(Ants, self).__init__()

    @classmethod
    def batch(cls, batch_size):
        batch_ants = np.array([Ants() for i in np.arange(0, batch_size)])
        return batch_ants

    def save(self, path=os.path.join(os.path.expanduser('~/Documents'), 'ANTS')):
        # variables
        today = datetime.datetime.today()
        f_name = str(today.strftime('%Y_%m_%d')) + '_ANTS.ants'
        save_path = os.path.join(path, f_name)

        os.makedirs(path, exist_ok=True)  # make dir
        with open(save_path, 'wb') as f:  # save self object
            pickle.dump(self, f)

    @classmethod
    def load(cls, path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
