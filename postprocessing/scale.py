import numpy as np
import postprocessing.__postprocessing as postprocessing


class Scale(postprocessing.Postprocessing):
    def __init__(self):
        super(Scale, self).__init__()

    def ts_to_sec(self):
        # variables
        _start = 0
        _duration_s = (self.timestamps[-1] - self.timestamps[0]) / (1000000 * 60)

        self.time = np.linspace(start=_start, stop=_duration_s, num=self.sample_frequency * _duration_s)
