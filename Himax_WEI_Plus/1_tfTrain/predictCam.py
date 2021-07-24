import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense
from tensorflow.keras.layers import Activation, BatchNormalization, Flatten
from tensorflow.keras.models import Sequential
from keras.models import Model
from functools import partial
import cv2
import numpy as np

# AUTOTUNE = tf.data.experimental.AUTOTUNE

# img_rows = 100
# img_cols = 100
# n_class = 2

# def EDGE(width, height, depth, classes):
#   input_shape = (width, height, depth)
#   model=Sequential()
#   #Conv1
#   model.add(Conv2D(filters=16, 
#                   kernel_size=(3, 3), 
#                   padding="same",  
#                   input_shape=input_shape))
#   model.add(BatchNormalization())
#   model.add(Activation("relu"))
#   model.add(MaxPooling2D())

#   #Conv2
#   model.add(Conv2D(filters=32, 
#                   kernel_size=(3, 3), 
#                   padding="same", 
#                   input_shape=input_shape))
#   model.add(BatchNormalization())
#   model.add(Activation("relu"))
#   model.add(MaxPooling2D())

#   #Conv3
#   model.add(Conv2D(filters=32, 
#                   kernel_size=(3, 3), 
#                   padding="same", 
#                   input_shape=input_shape))
#   model.add(BatchNormalization())
#   model.add(Activation("relu"))
#   model.add(MaxPooling2D())
#   # Model create #2(continue)

#   #FC1
#   model.add(Flatten())
#   model.add(Dense(64))
#   model.add(BatchNormalization())
#   model.add(Activation("relu"))

#   #FC2
#   model.add(Dense(classes))
#   model.add(Activation("softmax"))

#   return model

import cv2
from keras.optimizers import *
from keras.models import Model
from keras.layers import *
from keras.activations import *
from keras.callbacks import *

img_rows = 96
img_cols = 96
n_class = 2


def get_conv_block(tensor, channels, strides, alpha=1.0, name=''):
    channels = int(channels * alpha)

    x = Conv2D(channels,
               kernel_size=(3, 3),
               strides=strides,
               use_bias=False,
               padding='same',
               name='{}_conv'.format(name))(tensor)
    x = BatchNormalization(name='{}_bn'.format(name))(x)
    x = Activation('relu', name='{}_act'.format(name))(x)
    return x


def get_dw_sep_block(tensor, channels, strides, alpha=1.0, name=''):
    """Depthwise separable conv: A Depthwise conv followed by a Pointwise conv."""
    channels = int(channels * alpha)

    # Depthwise
    x = DepthwiseConv2D(kernel_size=(3, 3),
                        strides=strides,
                        use_bias=False,
                        padding='same',
                        name='{}_dw'.format(name))(tensor)
    x = BatchNormalization(name='{}_bn1'.format(name))(x)
    x = Activation('relu', name='{}_act1'.format(name))(x)

    # Pointwise
    x = Conv2D(channels,
               kernel_size=(1, 1),
               strides=(1, 1),
               use_bias=False,
               padding='same',
               name='{}_pw'.format(name))(x)
    x = BatchNormalization(name='{}_bn2'.format(name))(x)
    x = Activation('relu', name='{}_act2'.format(name))(x)
    return x


def MobileNet(shape, num_classes, alpha=1.0, include_top=True, weights=None):
    x_in = Input(shape=shape)

    x = get_conv_block(x_in, 32, (2, 2), alpha=alpha, name='initial')

    layers = [
        (64, (1, 1)),
        (128, (2, 2)),
        (128, (1, 1)),
        (256, (2, 2)),
        (256, (1, 1)),]
    #     (512, (2, 2)),
    #     *[(512, (1, 1)) for _ in range(5)],
    #     (1024, (2, 2)),
    #     (1024, (2, 2))
    # ]

    for i, (channels, strides) in enumerate(layers):
        x = get_dw_sep_block(x, channels, strides, alpha=alpha, name='block{}'.format(i))

    if include_top:
        x = GlobalAvgPool2D(name='global_avg')(x)
        x = Dense(num_classes, activation='softmax', name='softmax')(x)

    model = Model(inputs=x_in, outputs=x)

    if weights is not None:
        model.load_weights(weights, by_name=True)

    return model




if __name__ == '__main__':
    model = MobileNet((img_rows,img_cols,1),n_class)
    print(model.summary())

    #load weights to this TensorFlow model
    model.load_weights('./my_model0721mobile.h5')

    cap = cv2.VideoCapture(1)

    while True:
      ret, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
      cv2.imshow("Gray", gray)
      gray = cv2.resize(gray, (img_rows, img_cols), interpolation=cv2.INTER_CUBIC)
      reshapeimg = gray.reshape(1,img_rows, img_cols, 1) 
      transimg = reshapeimg.astype('float32')
      predict = model.predict(transimg)
      print(predict)
      print(np.argmax(predict))
      if cv2.waitKey(1) & 0xFF == ord('q'): break
    cap.release()
    cv2.destroyAllWindows()
