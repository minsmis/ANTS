import tensorflow as tf


class TextClassifier(tf.keras.models.Model):
    VOCAB_SIZE = 1000
    def __init__(self):
        super(TextClassifier, self).__init__()

        self.encoder = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE)