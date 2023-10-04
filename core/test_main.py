import core.ants as ants

path = ['/home/ms/Documents/Python/ANTS/sample_dataset/cerebellum_wave_ctx_3_lh_fc_4hr.mat',
        '/home/ms/Documents/Python/ANTS/sample_dataset/cerebellum_wave_fn_3_lh_fc_4hr.mat']
figure_path = '/home/ms/Documents/Python/ANTS/figures'

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


batch_ants = ants.Ants.batch(batch_size=len(path))
[batch_ants[i].callNeuralynx(path=path[i]) for i, _ in enumerate(batch_ants)]
[batch_ants[i].downsampling(target_fs=2000) for i, _ in enumerate(batch_ants)]
[batch_ants[i].normalization(method='rms') for i, _ in enumerate(batch_ants)]
# [batch_ants[i].waveletTransform(duration=[0, 10]) for i, _ in enumerate(batch_ants)]
[batch_ants[i].spectrogram(sduration=[0, 10], nperseg=1000, pscale='log') for i, _ in enumerate(batch_ants)]
f, m, sem = ants.Ants.sem(batch=batch_ants)
ants.Ants().powerSpectrum(freqs=f, mean=m, sem=sem, xscope=[0, 200])
