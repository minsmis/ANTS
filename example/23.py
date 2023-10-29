import core.ants as ants

""" Usage example """

path = r'/Users/minseokkim/Documents/Python/ANTS/sample_dataset'
figure_path = r'/Users/minseokkim/Documents/Python/ANTS/figures'

path_list = ants.dirprep.DirPrep.get_data_directory(superior_path=path, expander='mat')  # get data directories

batch_ants = ants.Ants.make(batch_size=len(path_list))  # make 'ants' as worker

[batch_ants[i].call_neuralynx(path=path_list[i]) for i, _ in enumerate(batch_ants)]  # import neuralynx

[batch_ants[i].downsampling(target_fs=2000) for i, _ in enumerate(batch_ants)]  # downsampling
[batch_ants[i].normalization(method='rms') for i, _ in enumerate(batch_ants)]  # normalization
[batch_ants[i].bandpass_butter(target_band=[40, 100]) for i, _ in enumerate(batch_ants)]  # bandpass filter

[batch_ants[i].wavelet(duration=[0, 10]) for i, _ in enumerate(batch_ants)]  # calc wavelet spectrogram
f, m, sem = ants.Ants.sem(batch=batch_ants)  # calculate sem
storage = ants.Ants().power_spectrum(freqs=f, mean=m, sem=sem, xscope=[0, 200])  # draw power spectrum with sem
#
# # calc multitaper spectrogram
# [batch_ants[i].spectrogram(duration=[0, 10], nperseg=1000, pscale='log') for i, _ in enumerate(batch_ants)]
# f, m, sem = ants.Ants.sem(batch=batch_ants)  # calculate sem
# storage = ants.Ants().power_spectrum(freqs=f, mean=m, sem=sem, xscope=[0, 200])  # draw power spectrum with sem
#
# batch_ants[0].plot_eeg(duration=[0, 0.5], filter=[40, 100])  # plot sample eeg
#
# # preferred phase
# _units_eeg_idx = [0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
# spikes = ants.Ants.get_spikes(superior_path=path, sample_frequency=batch_ants[0].sample_frequency, scale='idx')
# preferred_phase = [(ants.Ants.preferred_phase(batch_ants[eeg].bandpass_samples,
#                                               batch_ants[eeg].sample_frequency, spikes[i]))
#                    for (i, _), eeg in zip(enumerate(spikes), _units_eeg_idx)]
#
# # cell type classification
# spikes_s = ants.Ants.get_spikes(superior_path=path, scale='sec')
# is_pc = [ants.Ants.classify(spikes_s[i], mode='pc') for i, _ in enumerate(spikes_s)]
