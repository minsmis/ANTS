import core.antslogger as log
import timefrequency.__timefrequency as timefreq

import scipy as sp
import numpy as np


class Multitaper(timefreq.TimeFrequency):
    def __init__(self):
        super(Multitaper, self).__init__()

    # def multitapers(self, **kwargs):  # In development
    #
    #     if 'duration' in kwargs:
    #         duration_s = kwargs.get('duration')
    #         if isinstance(duration_s, list):
    #             duration_ts = [int((dur * self.sample_frequency) - 1) if dur > 0 else 0 for dur in duration_s]
    #             samples = self.samples[duration_ts[0]:duration_ts[-1]]  # slicing samples
    #         else:
    #             log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
    #             samples = self.samples  # Default samples
    #     else:
    #         samples = self.samples  # Default samples
    #
    #     # variables
    #     save_interval = 500
    #     times2save = np.arange(0, len(samples) - save_interval, save_interval)
    #     timewin = 1000  # in ms
    #
    #     # convert time points to indices
    #     timewinidx = round(timewin / (1000 / self.sample_frequency))
    #     nw_product = 100
    #     # determines the frequency smoothing, given a specified time window
    #
    #     # define tapers
    #     tapers = sp.signal.windows.dpss(M=timewinidx, NW=nw_product, Kmax=nw_product * 2)
    #     # define frequencies for FFT
    #     f = np.linspace(0, self.sample_frequency / 2, int(np.floor(timewinidx / 2)))
    #
    #     # initialize output matrix
    #     multitaper_tf = np.zeros((int(np.floor(timewinidx / 2)), len(times2save)))
    #
    #     # loop through time bins
    #     for ti in np.arange(0, len(times2save)):
    #         # initialize power vector (over tapers)
    #         taperpow = np.zeros((int(np.floor(timewinidx / 2)),))
    #
    #         # loop through tapers
    #         for tapi in np.arange(0, np.size(tapers, 0)):
    #             # window and taper data, and get power spectrum
    #             data = np.apply_along_axis((lambda a, b: a * b), 1,
    #                                        np.atleast_2d(samples[times2save[ti]:
    #                                                              times2save[ti] + (save_interval * 2)]).T,
    #                                        tapers[tapi, :])  # 50 % overlap window
    #             pow = sp.fft.fft(data, timewinidx) / timewinidx
    #             pow = pow[:, 1:int(np.floor(timewinidx / 2) + 1)]
    #             taperpow = taperpow + np.mean(np.abs(pow) ** 2, 0)
    #
    #         # finally, get power from the closest frequency
    #         multitaper_tf[:, ti] = taperpow / (np.size(tapers, 0) - 1)
    #
    #     # db-correct
    #     db_multitaper_tf = 10 * np.log10(multitaper_tf)
    #
    #     # save results
    #     self.waves = db_multitaper_tf
    #     self.waves_freqs = f
    #     self.f_power = np.mean(np.log10(multitaper_tf), 1)
    #     self.t_power = np.mean(np.log10(multitaper_tf), 0)

    def spectrogram(self, **kwargs):

        # kwargs
        samples = kwargs.get('samples') if 'samples' in kwargs else self.samples
        fs = kwargs.get('fs') if 'fs' in kwargs else self.sample_frequency
        seg = kwargs.get('nperseg') if 'nperseg' in kwargs else int(np.floor(len(samples) / 2))
        overlap = kwargs.get('noverlap') if 'noverlap' in kwargs else int(np.floor(seg / 4.5))
        window = kwargs.get('window') if 'window' in kwargs else 'hann'
        nfft = kwargs.get('nfft') if 'nfft' in kwargs else seg
        scaling = kwargs.get('scaling') if 'scaling' in kwargs else 'spectrum'
        mode = kwargs.get('mode') if 'mode' in kwargs else 'complex'

        if 'duration' in kwargs:
            duration_s = kwargs.get('duration')
            if isinstance(duration_s, list):
                duration_ts = [int((dur * fs) - 1) if dur > 0 else 0 for dur in duration_s]
                samples = samples[duration_ts[0]:duration_ts[-1]]  # slicing samples
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
                samples = samples  # Default samples
        else:
            samples = samples  # Default samples

        # spectrogram
        freqs, times, spectrum = sp.signal.spectrogram(x=samples, fs=fs, nperseg=seg, noverlap=overlap,
                                                       window=window, nfft=nfft, scaling=scaling, mode=mode)

        # save spectrum
        if 'pscale' in kwargs:
            power_scale = kwargs.get('pscale')
            if isinstance(power_scale, str) and power_scale == 'log':
                self.f_power = 10 * np.log10(np.mean(np.abs(spectrum) ** 2, 1))
            else:
                self.f_power = np.mean(np.abs(spectrum) ** 2, 1)
        else:
            self.f_power = np.mean(np.abs(spectrum) ** 2, 1)

        self.waves = spectrum
        self.t_power = np.mean(np.abs(spectrum) ** 2, 0)
        self.waves_freqs = freqs
