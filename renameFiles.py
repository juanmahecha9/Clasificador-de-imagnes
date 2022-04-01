import os

files = os.listdir('C:/Users/mahechacruz.6/OneDrive - Teleperformance/Desktop/procesamiento imagen clasificador/prueba')

for i in range(len(files)):
    os.rename('C:/Users/mahechacruz.6/OneDrive - Teleperformance/Desktop/procesamiento imagen clasificador/prueba/' + files[i], 'C:/Users/mahechacruz.6/OneDrive - Teleperformance/Desktop/procesamiento imagen clasificador/prueba/' + str(i) + '.jpg')