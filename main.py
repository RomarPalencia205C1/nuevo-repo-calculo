import os
import sys

# Agrega la carpeta 'src' al path para encontrar los modulos.
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from app.application import Application

if __name__ == "__main__":
    # Se define la ruta a la carpeta que contiene los archivos de datos.
    project_root = os.path.dirname(os.path.abspath(__file__))
    data_dir_path = os.path.join(project_root, "data")

    # Se instancia y se corre la aplicacion, pasandole el directorio de datos.
    app = Application(data_dir_path)
    app.run()