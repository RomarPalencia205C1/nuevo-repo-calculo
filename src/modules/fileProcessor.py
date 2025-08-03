import re
from core.customDataStructures import CustomList
from modules.numberIdentifier import NumberIdentifier

class FileProcessor:
    def __init__(self, filePath):
        self._filePath = filePath
        self._identifier = NumberIdentifier()

    def readFileAndProcess(self):
        processedMatrix = CustomList()
        try:
            with open(self._filePath, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    row = CustomList()
                    parts = re.split(r'[#,\s]+', line.strip())
                    for part in parts:
                        if part:
                            numericObject = self._identifier.identify(part)
                            row.append(numericObject)
                    processedMatrix.append(row)
        except FileNotFoundError:
            print(f"Error: El archivo '{self._filePath}' no fue encontrado.")
            return CustomList()
        
        print(f"Archivo procesado: {processedMatrix.size()} filas.")
        return processedMatrix