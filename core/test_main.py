import core.ants as ants

path = r'K:\Nlx2NRD\Spikeinterface\Data\2023-10-05_io_gfp_acute\lh'
figure_path = r'C:\Users\MinSeokKIM\Documents\Python\ANTS\figures'

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
batch_ants = ants.Ants.make(batch_size=len(path_list))  # make 'ants' as worker
[batch_ants[i].call_neuralynx(path=path_list[i]) for i, _ in enumerate(batch_ants)]  # import neuralynx
[batch_ants[i].downsampling(target_fs=2000) for i, _ in enumerate(batch_ants)]  # downsampling
[batch_ants[i].normalization(method='rms') for i, _ in enumerate(batch_ants)]  # normalization
[batch_ants[i].bandpass_butter(target_band=[40, 100]) for i, _ in enumerate(batch_ants)]  # bandpass filter
# [batch_ants[i].wavelet(duration=[0, 10]) for i, _ in enumerate(batch_ants)]  # calc wavelet spectrogram
# calc multitaper spectrogram
[batch_ants[i].spectrogram(duration=[0, 10], nperseg=1000, pscale='log') for i, _ in enumerate(batch_ants)]
f, m, sem = ants.Ants.sem(batch=batch_ants)  # calculate sem
ants.Ants().power_spectrum(freqs=f, mean=m, sem=sem, xscope=[0, 200])  # draw power spectrum with sem
batch_ants[0].plot_eeg(duration=[0, 0.5], filter=[40, 100])  # plot sample eeg

# preferred phase
_units_eeg_idx = [0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
spikes = ants.Ants.get_spikes(superior_path=path, sample_frequency=batch_ants[0].sample_frequency)
preferred_phase = [(ants.Ants.preferred_phase(batch_ants[eeg].bandpass_samples,
                                              batch_ants[eeg].sample_frequency, spikes[i]))
                   for (i, _), eeg in zip(enumerate(spikes), _units_eeg_idx)]
