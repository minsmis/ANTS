import extractor.caller as caller
import preprocessing.downsampling as downsampling
import preprocessing.filters as filters
import preprocessing.normalization as normalization
import timefrequency.wavelet as wavelet
import painter.plots as plots


# User interface
class ants(caller.CallTimeSeries, downsampling.Downsampling,
           filters.Filters, normalization.Normalization, wavelet.Wavelet,
           plots.Plots):
    def __init__(self):
        super(ants, self).__init__()
