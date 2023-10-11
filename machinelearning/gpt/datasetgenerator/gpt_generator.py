import os
import csv
import numpy as np
import tensorflow as tf

data = ['import', 'normalize', 'downsample', 'spectrum', 'plot']
data_path = '/home/ms/Documents/Python/ANTS/machinelearning/gpt/datasetgenerator/pregenrated_synonyms/{}_synonyms.csv'
words = []
labels = []

for label, d in enumerate(data):
    d_path = data_path.format(d)

    with open(d_path, 'r', encoding='utf-8') as f:  # open csv
        reader = csv.reader(f)

        wrds = []
        [wrds.extend(word) for word in reader]  # get synonyms
        wrds = np.array(wrds[1:])
        wrds = [w.lower() for w in wrds]  # lowercase
        words.extend(wrds)  # storage
        labels.extend(np.zeros(len(wrds)) + label)  # labels

words_tensor = tf.constant(words)
labels_tensor = tf.constant(labels)

keyword_ds = tf.data.Dataset.from_tensor_slices((words_tensor, labels_tensor))
keyword_ds.save(os.path.join(os.getcwd(), 'keyword_ds'))