import core.ants as ants

path = '/home/ms/Documents/Python/ANTS/sample_dataset'
figure_path = '/Users/minseokkim/Documents/Python/ANTS/figures'

# # call neuralynx timeseries data
# ant = ants.Ants()
#
# # path_list = ant.callAllFolders(path)
#
# ant.callNeuralynx(path=path)
#
# print('Sample Frequency: ', ant.sample_frequency)
#
# #  downsample to 2000 Hz
# ant.downsampling(target_fs=2000)
#
# print('Sample Frequency after Downsampling: ', ant.sample_frequency)
#
# # normalization with rms
# ant.normalization(method='rms')
#
# # bandpassfilter
# ant.bandpassButter(target_band=[4, 12])
#
# print('Samples: ', ant.samples)
# print('Samples after applying theta bandpass filter: ', ant.bandpass_samples)
#
# # wavelet time frequency
# # ant.waveletTransform(duration=[0, 10])
# ant.spectrogram(sduration=[0, 10], nperseg=2000, pscale='log')
# print('power spectrum finished')
#
# # draw and save the power spectrum as png
# ant.powerSpectrum(xscope=[0, 200])
# print('plot finished')


######

path_list = ants.dirprep.DirPrep.get_data_directory(superior_path=path, expander='mat')  # get data directories
batch_ants = ants.Ants.batch(batch_size=len(path_list))  # make 'ants' as worker
[batch_ants[i].call_neuralynx(path=path_list[i]) for i, _ in enumerate(batch_ants)]  # import neuralynx
[batch_ants[i].downsampling(target_fs=2000) for i, _ in enumerate(batch_ants)]  # downsampling
[batch_ants[i].normalization(method='rms') for i, _ in enumerate(batch_ants)]  # normalization
# [batch_ants[i].wavelet(duration=[0, 10]) for i, _ in enumerate(batch_ants)]  # calc wavelet spectrogram
# calc multitaper spectrogram
[batch_ants[i].spectrogram(sduration=[0, 10], nperseg=1000, pscale='log') for i, _ in enumerate(batch_ants)]
f, m, sem = ants.Ants.sem(batch=batch_ants)  # calculate sem
ants.Ants().power_spectrum(freqs=f, mean=m, sem=sem, xscope=[0, 200])  # draw power spectrum with sem
