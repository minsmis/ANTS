import os
import painter.__painter as painter
import timefrequency.wavelet as wavelet
import matplotlib.pyplot as plt


class Plots(painter.Painter):
    def __init__(self):
        super(Plots, self).__init__()

    def powerSpectrum(self, directory):
        f_power = wavelet.Wavelet.toFPower(self.waves)
        freq = self.waves_freqs

        fig, ax = plt.subplots()
        ax.plot(freq, f_power)
        fig.savefig(os.path.join(directory, 'power_spectrum.png'))
