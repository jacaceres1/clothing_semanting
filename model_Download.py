import os
import gdown

# URL del archivo en Google Drive
file_url = 'https://drive.google.com/file/d/1JM1gbJZTGMRI1lJYo-y1E51z-izUbUZq/view?usp=sharing'

# Crear la carpeta 'model' si no existe
if not os.path.exists('model'):
    os.makedirs('model')

# Descargar el archivo y guardarlo en la carpeta 'model'
output_file = 'model/cloth_segm.pth'
gdown.download(file_url, output_file, quiet=False)
