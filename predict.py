
import numpy as np
import time
from datetime import datetime
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
    #En esta funcion la idea es pasar la imagen  y poder definir a que tipo representa antes de eliminar la pagina del pdf
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x)
    result = array[0]
    answer = np.argmax(result)
    ans = ''
    if answer == 0:
        print("Predicción: Basura")
        ans = 'Otros'
    elif answer == 1:
        print("Predicción: DNI")
        ans = 'DNI'
    else:
        print("Predicción: Otro")
        ans = 'No clasiificado'
    return ans

path = 'C:/Users/mahechacruz.6/OneDrive - Teleperformance/Desktop/procesamiento imagen clasificador/prueba'
register = 'C:/Users/mahechacruz.6/OneDrive - Teleperformance/Desktop/procesamiento imagen clasificador'

if os.path.exists(register + '/' + 'resultados.csv'):
    os.remove(register + '/' + 'resultados.csv')
time.sleep(5)

with open(register + '/' + 'resultados.csv', 'a') as f:
        f.write('Nombre del archivo; resultado de la clasificaicon; tiempo de espera;then;now\n')
        f.close()

files = os.listdir(path)

for file in files:
    print(file)
    then = datetime.now() 
    result = predict(path + '/' + file)
    now = datetime.now()
    delta = now - then
    with open(register + '/' + 'resultados.csv', 'a') as f:
        f.write(file + ';' + result + ';' + str(delta.seconds) + ';' + str(then) + ';' + str(now) + '\n')
        f.close()
