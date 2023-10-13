import numpy as np
import postprocessing.__postprocessing as postprocessing


class Scale(postprocessing.Postprocessing):
    def __init__(self):
        super(Scale, self).__init__()

    @classmethod
    def ts_to_sec(cls, timestamps, sample_frequency):
        # variables
        _start = 0
        _duration_s = (timestamps[-1] - timestamps[0]) / (1000000 * 60)

        time = np.linspace(start=_start, stop=_duration_s, num=sample_frequency * _duration_s)
        return time
