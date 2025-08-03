from modules.fileProcessor import FileProcessor
from core.numericValue import NumericValue

class Application:
    def __init__(self, data_file_path):
        self._data_file_path = data_file_path

    def run(self):
        print("--- Proyecto de Calculo Numerico ---")
    
        processor = FileProcessor(self._data_file_path)
        dataMatrix = processor.readFileAndProcess()
    
        if dataMatrix.size() == 0:
            print("No se pudieron procesar los datos. Finalizando programa.")
            return

        self._analyzeData(dataMatrix)

    def _analyzeData(self, dataMatrix):
        for i in range(dataMatrix.size()):
            row = dataMatrix.get(i)
            print(f"\n--- Analisis Fila {i+1} ---")
            for j in range(row.size()):
                item = row.get(j)
                if isinstance(item, NumericValue):
                    print(f"  Dato[{j}]: '{item.getRawValue()}'")
                    print(f"    -> Sistema: {type(item).__name__}")
                    print(f"    -> Normalizado: {item.getNormalizedForm()}")
                    print(f"    -> Cifras Significativas: {item.countSignificantFigures()}")
                    print(f"    -> Operaciones Posibles: {item.getPossibleOperations()}")
                else:
                    print(f"  Dato[{j}]: '{item}' (ERROR: No reconocido)")