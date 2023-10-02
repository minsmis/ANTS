function [waves, waves_freqs] = pyCwt(samples, sample_frequency)

    [waves, waves_freqs] = cwt(samples, "morse", sample_frequency);

end