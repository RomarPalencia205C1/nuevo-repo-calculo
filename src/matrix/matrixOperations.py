from core.customDataStructures import CustomList
from core.numericValue import NumericValue

class Matrix:
    def __init__(self, rows, cols, initialValue=None):
        self._rows = rows
        self._cols = cols
        self._grid = CustomList()
        for i in range(rows):
            row = CustomList()
            for j in range(cols):
                row.append(initialValue)
            self._grid.append(row)

    def setElement(self, row, col, value):
        if not isinstance(value, NumericValue):
            raise TypeError("El valor a insertar debe ser un objeto NumericValue.")
        self._grid.get(row).get(col)

    def getElement(self, row, col):
        return self._grid.get(row).get(col)
    
class MatrixOperations:
    def add(self, matrixA, matrixB):
        pass

    def subtract(self, matrixA, matrixB):
        pass