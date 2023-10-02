import preprocessing.__preprocessing as preprocessing
import numpy as np


class Normalization(preprocessing.Preprocessing):
    def __init__(self):
        super(Normalization, self).__init__()

    def normalization(self, method):
        if method == 'rms':
            root_mean_square = np.sqrt(np.mean(self.samples ** 2))
            self.samples /= root_mean_square
        elif method == 'zscore':
            pass
