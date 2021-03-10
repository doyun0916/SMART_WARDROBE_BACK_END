import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, GlobalAveragePooling2D, AveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import regularizers
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import SGD

n = os.getcwd()
PATH = os.path.join(os.path.dirname(n), 'classi')
saved = os.path.join(PATH, 'saved')
test = os.path.join(PATH, 'test')
# test = os.path.join(PATH, 'img_00000011_class2.jpg')
# print(test)
# print(category_dir)

batch_size = 1
epochs = 30
IMG_HEIGHT = 150
IMG_WIDTH = 150

test_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our test data

test_data_gen = test_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=test,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                            class_mode='categorical'
                                                           )


model = tf.keras.models.load_model(saved)

print(model.predict(test_data_gen))
print(np.argmax(model.predict(test_data_gen), axis= 1))

