# checkHandWrittenDigits

Python-Flask server for analyse image with one hand written digit

To analyse images, I use [tensorflow](https://www.tensorflow.org/)

## Technologies

Server -> Python 3.8 with Flask 2.2.3

Model -> Tensorflow-macos 2.9

## Model

### dataset

I use the [MNIST](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_MNIST) dataset

### training

The model is train until it reached 0.99 accuracy

I use the adam algorithm for the optimizer and sparse_categorical_crossentropy for the loss

## How to use

You can install dependencies with the following command :

```bash
pip install -r requirements.txt
```

and run the server :
```bash
python server/app.py
```
