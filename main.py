import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from app.application import Application

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    file_name = "prueba_20240515_001.txt"
    data_file_path = os.path.join(project_root, "data", file_name)

    app = Application(data_file_path)
    app.run()