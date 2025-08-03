import os
import random

class DataGenerationService:
    # Metodo para generar los datos de un sistema de ecuaciones N x (N+1)
    def generateLinearSystemData(self, size: int = 3):
        """
        Genera una lista de listas con datos numericos para un sistema de ecuaciones.

        ->@param size: El numero de ecuaciones e incognitas (ej. 3 para un sistema 3x3).
        ->@return: Una lista de listas de numeros.
        """
        if size <= 1:
            raise ValueError("El tamaño del sistema debe ser mayor que 1.")
        
        # Generamos una matriz de N x (N+1) con enteros aleatorios.
        return [[random.randint(-20, 20) for _ in range(size + 1)] for _ in range(size)]

    # Metodo para escribir los datos generados a un archivo.
    def writeDataToFile(self, data: list, filename: str):
        """
        Escribe los datos en un archivo dentro de la carpeta 'data',
        usando comas como separadores.

        ->@param data: La lista de listas con los datos.
        ->@param filename: El nombre del archivo a crear (ej. 'sistema_aleatorio.txt').
        """
        # Construimos la ruta completa al archivo dentro de la carpeta 'data'.
        file_path = os.path.join("data", filename)

        try:
            with open(file_path, 'w') as f:
                for i, row in enumerate(data):
                    # Convertimos cada numero de la fila a string y los unimos con comas.
                    line = ", ".join(map(str, row))
                    f.write(line)
                    # Añadimos un salto de linea para todas las filas excepto la ultima.
                    if i < len(data) - 1:
                        f.write('\n')
            
            print(f"Archivo '{filename}' generado con exito en la carpeta 'data'.")

        except Exception as e:
            print(f"Error al escribir el archivo: {e}")