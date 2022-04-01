# Crear
python -m virtualenv clasificador
call clasificador\Scripts\activate
pip install -r bin\requirements.txt


# Capturar las librerias
call clasificador\Scripts\activate 
pip freeze > bin\requirements.txt