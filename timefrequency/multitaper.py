import numpy as np

import core.ants as ants


class Multitaper(ants.Ants):
    def __init__(self):
        super(Multitaper, self).__init__()

    def multitaper(self, **kwargs):
        # set multitaper parameters

        # split data into segments

        # compute DPSS tapers

        # multiply the data segment by the DPSS tapers

        # compute the spectrum for each tapered segment

        # take the mean of the tapered spectra
        pass

    def process_spectrogram_params(self, fs, nfft, frequency_range, window_start, datawin_size):
        """ Helper function to create frequency vector and window indices
                Arguments:
                     fs (float): sampling frequency in Hz  -- required
                     nfft (int): length of signal to calculate fft on -- required
                     frequency_range (list): 1x2 list - [<min frequency>, <max frequency>] -- required
                     window_start (1xm np array): array of timestamps representing the beginning time for each
                                                  window -- required
                     datawin_size (float): seconds in one window -- required
                Returns:
                    window_idxs (nxm np array): indices of timestamps for each window
                                                (nxm where n=number of windows and m=datawin_size)
                    stimes (1xt np array): array of times for the center of the spectral bins
                    sfreqs (1xf np array): array of frequency bins for the spectrogram
                    freq_inds (1d np array): boolean array of which frequencies are being analyzed in
                                              an array of frequencies from 0 to fs with steps of fs/nfft
            """

        # create frequency vector
        df = fs / nfft
        sfreqs = np.arange(0, fs, df)

        # Get frequencies for given frequency range
        freq_inds = (sfreqs >= frequency_range[0]) & (sfreqs <= frequency_range[1])
        sfreqs = sfreqs[freq_inds]

        # Compute times in the middle of each spectrum
        window_middle_samples = window_start + round(datawin_size / 2)
        stimes = window_middle_samples / fs

        # Get indexes for each window
        window_idxs = np.atleast_2d(window_start).T + np.arange(0, datawin_size, 1)
        window_idxs = window_idxs.astype(int)

        return [window_idxs, stimes, sfreqs, freq_inds]
