import numpy as np


class TimeSeries:
    def __init__(self):
        super(TimeSeries, self).__init__()

        # variables
        self.header = list
        self.sample_frequency = int
        self.samples = np.ndarray
        self.timestamps = np.ndarray

        self.bandpass_samples = np.ndarray

        self.waves = np.ndarray
        self.waves_freqs = np.ndarray