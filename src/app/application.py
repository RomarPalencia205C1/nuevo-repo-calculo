import os
import sys
from modules.fileProcessor import FileProcessor
from services.loggingService import LoggingService
from services.reportService import ReportService 

class Application:
    # El constructor ahora recibe la ruta al directorio de datos.
    def __init__(self, data_directory_path):
        self._data_dir_path = data_directory_path
        self._logger = LoggingService()
        self._report_service = ReportService() 

    # El metodo run ahora contiene la logica para procesar todos los archivos.
    def run(self):
        try:
            # 1. Verificar si el directorio 'data' existe.
            if not os.path.isdir(self._data_dir_path):
                print(f"Error: El directorio '{self._data_dir_path}' no fue encontrado.")
                return

            # 2. Obtener una lista de todos los archivos .txt en el directorio.
            files_to_process = [f for f in os.listdir(self._data_dir_path) if f.endswith(".txt")]

            if not files_to_process:
                print(f"No se encontraron archivos .txt en la carpeta '{self._data_dir_path}'.")
                return

            print(f"Se encontraron {len(files_to_process)} archivo(s) para procesar.")

            # 3. Iterar sobre cada archivo y ejecutar el analisis.
            for file_name in files_to_process:
                print(f"\n{'='*50}")
                print(f"PROCESANDO ARCHIVO: {file_name}")
                print(f"{'='*50}")
                
                file_path = os.path.join(self._data_dir_path, file_name)
                
                processor = FileProcessor(file_path)
                dataMatrix = processor.readFileAndProcess()
            
                if dataMatrix.size() > 0:
                    self._report_service.generateFullReport(dataMatrix, file_name)

            print(f"\n{'='*50}")
            print("Todos los archivos han sido procesados.")

        except Exception as e:
            print(f"\nHa ocurrido un error grave. Revise 'archivo.log' para mas detalles.")
            self._logger.logError(e)