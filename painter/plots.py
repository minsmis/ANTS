import os

import numpy as np

import core.antslogger as log
import painter.__painter as painter
import timefrequency.wavelet as wavelet
import postprocessing.power as power
import matplotlib.pyplot as plt


class Plots(painter.Painter):
    def __init__(self):
        super(Plots, self).__init__()

    @classmethod
    def powerSpectrum(cls, **kwargs):
        figure_path = os.path.join(os.path.dirname(os.getcwd()), 'figures')
        os.makedirs(figure_path, exist_ok=True)  # make 'figures' directory

        fig, ax = plt.subplots()

        # plot spectrum
        if 'mean' and 'sem' and 'freqs' in kwargs:
            freqs = kwargs.get('freqs')
            mean = kwargs.get('mean')
            sem = kwargs.get('sem')
            if isinstance(freqs, np.ndarray) and isinstance(mean, np.ndarray) and isinstance(sem, np.ndarray):
                ax.fill_between(freqs, mean - sem, mean + sem, alpha=0.5)
                ax.plot(freqs, mean)
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
        else:
            f_power = power.Power.toFreqPower(waves=self.waves)
            freqs = self.waves_freqs
            ax.plot(freqs, f_power)

        # save spectrum
        if 'directory' in kwargs:
            directory = kwargs.get('directory')
            if isinstance(directory, str):
                fig.savefig(os.path.join(directory, 'power_spectrum.png'))
            else:
                log.logger_handler.throw_warning(warn_code='0004', warn_msg='Default Path Selected')
                fig.savefig(os.path.join(figure_path, 'power_spectrum.png'))
        else:
            fig.savefig(os.path.join(figure_path, 'power_spectrum.png'))
