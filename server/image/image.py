import numpy as np
from PIL import Image, ImageOps

def transformImg(img_path) -> np.ndarray:
    img = Image.open(img_path)
    img = img.convert('L')
    img = img.resize((28, 28))
    img = ImageOps.invert(img)
    imgArray = np.expand_dims(np.array(img), axis=-1)
    imgArray = imgArray / 255.0
    imgArray = np.array(imgArray)
    imgArray = imgArray.reshape(1, 28, 28, 1)
    return imgArray