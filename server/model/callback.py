import tensorflow as tf

class Callback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('acc')>=0.99):
          print("\n99% accuracy reached!")
          self.model.stop_training = True