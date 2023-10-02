import postprocessing.__postprocessing as postprocessing
import core.antslogger as log
import numpy as np
import scipy as sp


class Power(postprocessing.Postprocessing):
    def __init__(self):
        super(Power, self).__init__()

    @classmethod
    def toFreqPower(cls, waves):
        f_power = np.mean((np.abs(waves)) ** 2, 1)
        return f_power

    @classmethod
    def toTimePower(cls, waves):
        t_power = np.mean((np.abs(waves)) ** 2, 0)
        return t_power

    @classmethod
    def stackPower(cls, ants):
        f_power_len = [len(Power.toFreqPower(ants[i].waves)) for i, ant in enumerate(ants)]
        max_len = max(f_power_len)
        freqs = ants[np.argmax(f_power_len)].waves_freqs

        # stack f_power
        stack = np.array([Power.toFreqPower(ants[i].waves) if f_power_len[i] == max_len else
                          np.append(Power.toFreqPower(ants[i].waves), np.repeat(np.nan, max_len - f_power_len[i]))
                          for i, ant in enumerate(ants)])
        return dict(frequency=freqs, stack=stack)

    @classmethod
    def sem(cls, **kwargs):
        if 'stack' in kwargs:
            stack_dict = kwargs.get('stack')
            freqs, stack = stack_dict['frequency'], stack_dict['stack']
        elif 'batch' in kwargs:
            batch = kwargs.get('batch')
            if isinstance(batch, np.ndarray):
                stack_dict = Power.stackPower(ants=batch)
                freqs, stack = stack_dict['frequency'], stack_dict['stack']
            else:
                log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
                return None
        else:
            log.logger_handler.throw_error(err_code='0003', err_msg='Value Error')
            return None

        mean = np.mean(stack, 0)
        se_m = sp.stats.sem(a=stack, nan_policy='omit')
        return freqs, mean, se_m