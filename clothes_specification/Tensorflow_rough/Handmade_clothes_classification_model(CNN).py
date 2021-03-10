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
category_dir = os.path.join(PATH, 'outer')
saved = os.path.join(PATH, 'saved')
test = os.path.join(PATH, 'test')
# test = os.path.join(PATH, 'img_00000011_class2.jpg')
# print(test)
# print(category_dir)

batch_size = 1
epochs = 90
IMG_HEIGHT = 150
IMG_WIDTH = 150

train_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our training data

test_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our test data

train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                           directory=category_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                           class_mode='categorical'
                                                          )

test_data_gen = test_image_generator.flow_from_directory(batch_size=batch_size,
                                                         directory=test,
                                                         shuffle=True,
                                                         target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                         class_mode='categorical'
                                                           )

# from PIL import Image
# test1 =tf.keras.preprocessing.image.load_img( test, grayscale=False, color_mode='rgb', target_size=(150, 150), interpolation='nearest')
# print(test1)
# test2 = tf.keras.preprocessing.image.img_to_array(test1)
# print(test2.ndim)
# image_batch, label_batch = next(train_data_gen)
# plt.imshow(image_batch[0], interpolation='nearest')
# plt.show()
# print(label_batch[0])


model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),    #3차원 layer
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Dropout(0.2),
    Flatten(),
    Dense(512, activation='relu'),      # 1차원 layer (logical regression)
    Dense(4, activation='softmax')
])

model.compile(optimizer='adam',          # gradient descent와 비슷한 종류의 친구들
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

history = model.fit(
    train_data_gen,
    steps_per_epoch=300, # batch_size,
    epochs=epochs
     # batch_size
)
print(model.predict(test_data_gen))
print(np.argmax(model.predict(test_data_gen), axis= 1))

model.save(saved)  # save() should be called out of strategy scope
# result = model.predict(test_data_gen)
# print('result:', result)

# # #overfitting 방지, data 늘리거나, dropout 적용
#
# sample_training_images, _ = next(test_data_gen)
#
# def plotImages(images_arr):
#     fig, axes = plt.subplots(1, 5, figsize=(20,20))
#     axes = axes.flatten()
#     for img, ax in zip( images_arr, axes):
#         ax.imshow(img)
#         ax.axis('off')
#     plt.tight_layout()
#     plt.show()
#
# plotImages(sample_training_images[:5])
