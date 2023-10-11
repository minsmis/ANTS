import core.antslogger as log
import timefrequency.__timefrequency as timefreq
import postprocessing.power as power
import os
import matlab
import matlab.engine as me
import numpy as np


class Wavelet(timefreq.TimeFrequency):

    def __init__(self):
        super(Wavelet, self).__init__()
        self.PATH_MATLAB_TIMEFREQUENCY = os.path.join(os.path.dirname(os.getcwd()),
                                                      'timefrequency', 'matlab_timefrequency')

    def wavelet(self, **kwargs):
        # Wavelet power spectrum - MATLAB
        matlab_engine = me.start_matlab()  # start matlab engine
        matlab_engine.cd(self.PATH_MATLAB_TIMEFREQUENCY)  # change directory to the custom matlab functions

        if 'duration' in kwargs:
            duration_s = kwargs.get('duration')
            if isinstance(duration_s, list):
                duration_ts = [int((dur * self.sample_frequency) - 1) if dur > 0 else 0 for dur in duration_s]
                # slicing and type casting to matlab double
                cwt_samples = matlab.double(self.samples[duration_ts[0]:duration_ts[-1]].tolist())
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
                cwt_samples = matlab.double(self.samples.tolist())  # type casting to matlab double
        else:
            cwt_samples = matlab.double(self.samples.tolist())  # type casting to matlab double

        cwt_sampling_frequency = matlab.double(self.sample_frequency)  # type casting to matlab double

        # run cwt
        waves, freqs = matlab_engine.pyCwt(cwt_samples, cwt_sampling_frequency, nargout=2)

        # save cwt results as numpy array
        self.waves = np.array(waves)
        self.waves_freqs = np.array(freqs).reshape(-1)
        self.f_power = power.Power.to_freq_power(waves=self.waves)
        self.t_power = power.Power.to_time_power(waves = self.waves)
