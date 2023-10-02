import preprocessing.__preprocessing as preprocessing


class Downsampling(preprocessing.Preprocessing):
    def __init__(self):
        super(Downsampling, self).__init__()

    def downsampling(self, target_fs):
        downsampling_coeff = int(self.sample_frequency / target_fs)

        self.sample_frequency = int(self.sample_frequency / downsampling_coeff)
        self.samples = self.samples[::downsampling_coeff]
        self.timestamps = self.timestamps[::downsampling_coeff]
