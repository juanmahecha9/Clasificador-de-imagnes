import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


from tensorflow.python.keras import backend as K

from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.optimizers import adam_v2
from tensorflow.python.keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

K.clear_session()

data_entrenamiento = r'C:/Users/mahechacruz.6/Red Neuronal/data/entrenamiento'
data_validacion = r'C:/Users/mahechacruz.6/Red Neuronal/data/validacion'

##Parameters
epocas = 20
altura, longitud = 150, 150
batch_size = 32
pasos = 1000
pasos_validacion = 200
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 2
lr = 0.0005

##Preprocessing data
entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
validacion_datagen = ImageDataGenerator(
    rescale=1. / 255
)

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

#Crear la red convolucional
cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same', input_shape=(altura, longitud, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))
cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))
cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy', optimizer=adam_v2.Adam(learning_rate=lr), metrics=['accuracy'])

cnn.fit(imagen_entrenamiento, steps_per_epoch=pasos, epochs=epocas, validation_data=imagen_validacion, validation_steps=pasos_validacion)

dir = r'C:/Users/mahechacruz.6/Red Neuronal/modelo'
if not os.path.exists(dir):
    os.mkdir(dir)
cnn.save(r'C:/Users/mahechacruz.6/Red Neuronal/modelo/modelo.h5')
cnn.save_weights(r'C:/Users/mahechacruz.6/Red Neuronal/modelo/pesos.h5')
