import os

import numpy as np

import core.antslogger as log
import core.ants as ants
import painter.__painter as painter
import postprocessing.power as power
import matplotlib.pyplot as plt


class Plots(painter.Painter):
    def __init__(self):
        super(Plots, self).__init__()

    def powerSpectrum(self, **kwargs):
        figure_path = os.path.join(os.path.dirname(os.getcwd()), 'figures')
        os.makedirs(figure_path, exist_ok=True)  # make 'figures' directory

        fig, ax = plt.subplots()

        # plot power sepctrum with sem
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
            ax.plot(self.waves_freqs, self.f_power)  # Default plot
            plt.autoscale(enable=True, axis='x', tight=True)
            plt.autoscale(enable=True, axis='y', tight=True)

        # X-axis (frequency) scope
        if 'xscope' in kwargs:
            frequency_scope = kwargs.get('xscope')
            if isinstance(frequency_scope, list) or isinstance(frequency_scope, np.ndarray):
                plt.xlim(frequency_scope[0], frequency_scope[-1])  # set xlim
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')

        # Y-axis (Power) scope
        if 'yscope' in kwargs:
            power_scope = kwargs.get('yscope')
            if isinstance(power_scope, list) or isinstance(power_scope, np.ndarray):
                plt.ylim(power_scope[0], power_scope[-1])  # set ylim
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')

        # Y-axis (Power) scale
        if 'yscale' in kwargs:
            y_scale_type = kwargs.get('yscale')
            if isinstance(y_scale_type, str):
                plt.yscale(y_scale_type)  # set y scale
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')

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
