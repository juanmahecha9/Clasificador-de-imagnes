# Crear
python -m virtualenv clasificador
call clasificador\Scripts\activate
pip install -r bin\requirements.txt


# Capturar las librerias
call clasificador\Scripts\activate 
pip freeze > bin\requirements.txt


# Como usar?
Crear una carpeta de data donde se van a tener las supcarpetas de imagenes a usar, si son mas de dos en el archivo clasificador  cambiar la variable clasee = 2 por el total de carpetas a usar tanto en entrenamiento como en validacion.
la estructura debe de verse asi
└───data
    ├───entrenamiento
    │   ├───caperta n-esima
    │   ├───carpeta 1
    │   └───carpeta 2
    └───validacion
        ├───caperta n-esima
        ├───carpeta 1
        └───carpeta 2
        
        
esto genera dentro de una carpeta modelo los archiovos .h5 a usar en el script de prediccion
