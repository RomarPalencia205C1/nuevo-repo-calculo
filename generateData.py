import sys
import os

# Agrega la carpeta 'src' al path para encontrar los modulos.
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from services.dataGenerationService import DataGenerationService

def main():
    # --- Parametros de Generacion ---
    # Se define una lista con los nombres de los archivos a generar.
    files_to_generate = ["sistema_A.txt", "sistema_B.txt", "sistema_C.txt"]
    
    # Se define el tamaño para los sistemas de ecuaciones.
    # Puedes cambiarlo si deseas, por ejemplo, a 4 para sistemas 4x4.
    system_size = 3 

    print(f"Iniciando la generacion de {len(files_to_generate)} archivos de prueba...")
    
    # 1. Instanciamos el servicio.
    generator = DataGenerationService()
    
    # 2. Iteramos sobre la lista de nombres para crear cada archivo.
    for file_name in files_to_generate:
        print(f"\nGenerando archivo: '{file_name}'...")
        try:
            # 3. Generamos los datos numericos para un sistema del tamaño especificado.
            system_data = generator.generateLinearSystemData(size=system_size)
            
            # 4. Escribimos los datos al archivo correspondiente.
            generator.writeDataToFile(system_data, file_name)
            
        except Exception as e:
            print(f"Ocurrio un error durante la generacion de '{file_name}': {e}")

    print("\nProceso de generacion finalizado.")

if __name__ == "__main__":
    main()