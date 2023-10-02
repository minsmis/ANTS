import core.ants as ants

path = '/home/ms/Documents/Python/ANTS/sample_dataset/cerebellum_waves.mat'
figure_path = '/home/ms/Documents/Python/ANTS/figures'

# call neuralynx timeseries data
# ant = ants.Ants()

# path_list = ant.callAllFolders(path)

# ants[0].callNeuralynx(path=path)

# print('Sample Frequency: ', ants[0].sample_frequency)
#
# #  downsample to 2000 Hz
# ants[0].downsampling(target_fs=2000)
#
# print('Sample Frequency after Downsampling: ', ants[0].sample_frequency)
#
# # normalization with rms
# ants[0].normalization(method='rms')
#
# # bandpassfilter
# ants[0].bandpassButter(target_band=[4, 12])
#
# print('Samples: ', ants[0].samples)
# print('Samples after applying theta bandpass filter: ', ants[0].bandpass_samples)
#
# # wavelet time frequency
# ants[0].waveletTransform(duration=[0, 10])
# print('wavelet end')
#
# # draw and save the power spectrum as png
# ants[0].powerSpectrum(directory='/home/ms/Documents/Python/ANTS/sample_dataset')

batch_ants = ants.Ants.batch(batch_size=10)
[batch_ants[i].callNeuralynx(path=path) for i, ant in enumerate(batch_ants)]
[batch_ants[i].downsampling(target_fs=2000) for i, ant in enumerate(batch_ants)]
[batch_ants[i].normalization(method='rms') for i, ant in enumerate(batch_ants)]
[batch_ants[i].waveletTransform(duration=[0, 10]) for i, ant in enumerate(batch_ants)]
f, m, sem = ants.Ants.sem(batch=batch_ants)
ants.Ants.powerSpectrum(freqs=f, mean=m, sem=sem, directory=figure_path)
