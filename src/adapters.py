import cv2
import numpy as np


def adapt_image(image):
    image_resized = cv2.resize(image, (224, 224))
    image_float = image_resized.astype('float32') / 255
    image_4d = np.expand_dims(image_float, 0)

    return image_4d
