import datetime
import os

# Tener en cuenta el paradigma orientado a objeto por cada servicio
class LoggingService:
    # Metodo para registrar un error en el archivo.log
    def logError(self, exception: Exception):
        # El programa de detectar o registrar en un archivo.log
        # el conteo de operaciones fallidas por interrupcion del sistema
        
        # --- CORRECCION AQUI ---
        # Se define el nombre del directorio y del archivo.
        log_directory = "log"
        log_filename = "archivo.log"
        
        # Se asegura que el directorio 'log' exista. Si no, lo crea.
        os.makedirs(log_directory, exist_ok=True)
        
        # Se construye la ruta completa al archivo de log.
        log_file_path = os.path.join(log_directory, log_filename)
        
        # 1. Obtenemos los datos para el formato del log.
        error_name = type(exception).__name__
        current_date = datetime.datetime.now().strftime('%Y%m%d')
        execution_serial = datetime.datetime.now().strftime('%H%M%S%f')
        
        # 2. Construimos el mensaje con el formato requerido.
        # Formato: NombreError_FechaActual_SerialEjecución: Error [...]
        log_message = (
            f"{error_name}_{current_date}_{execution_serial}: "
            f"Error [Excepcion: {str(exception)}]\n"
        )

        # 3. Añadimos el mensaje al archivo.log usando la nueva ruta.
        try:
            with open(log_file_path, 'a') as log_file:
                log_file.write(log_message)
        except Exception as e:
            # Si el logging falla, lo imprimimos en la consola.
            print(f"Error critico: No se pudo escribir en el archivo de log. Causa: {e}")