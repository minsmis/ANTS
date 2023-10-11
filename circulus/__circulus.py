import core.antstimeseries as timeseries


class Circulus(timeseries.TimeSeries):

    def __init__(self):
        super(Circulus, self).__init__()

    def get_phase(self, **kwargs):
        pass

    @classmethod
    def phase(cls, samples, sample_frequency, **kwargs):
        pass

    def get_preferred_phase(self, spike_peak_ts, **kwargs):
        pass
