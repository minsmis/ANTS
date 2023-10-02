import core.ants as ants

path = '/Users/minseokkim/Documents/Python/ANTS/sample_dataset/cerebellum_waves.mat'

# call neuralynx timeseries data
ant = ants.ants()
# path_list = ant.callAllFolders(path)
ant.callNeuralynx(path=path)

print('Sample Frequency: ', ant.sample_frequency)

#  downsample to 2000 Hz
ant.downsampling(target_fs=2000)

print('Sample Frequency after Downsampling: ', ant.sample_frequency)

# normalization with rms
ant.normalization(method='rms')

# bandpassfilter
ant.bandpassButter(target_band=[4, 12])

print('Samples: ', ant.samples)
print('Samples after applying theta bandpass filter: ', ant.bandpass_samples)

# wavelet time frequency
ant.waveletTransform(duration=[0, 10])
print('wavelet end')

# draw and save the power spectrum as png
ant.powerSpectrum(directory='/Users/minseokkim/Documents/Python/ANTS/sample_dataset')