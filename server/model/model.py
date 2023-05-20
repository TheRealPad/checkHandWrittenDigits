import tensorflow as tf
import numpy as np
from model.callback import Callback

class HandWrittenModel():
    def __init__(self) -> None:
        mnist = tf.keras.datasets.mnist
        (self.x_train, self.y_train),(self.x_test, self.y_test) = mnist.load_data()
        self.x_train  = self.x_train / 255.0
        self.x_test = self.x_test / 255.0
        self.model = any

    def createModel(self) -> None:
        callbacks = Callback()
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['acc'])
        self.model.fit(self.x_train, self.y_train, epochs=10, callbacks=[callbacks])
        self.model.evaluate(self.x_test, self.y_test)

    def analyseImage(self, digit) -> int:
        classification = self.model.predict(digit)
        print(classification[0])
        return np.argmax(classification[0])