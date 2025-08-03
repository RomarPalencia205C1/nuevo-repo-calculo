import numpy as np

class Matrix:
    def __init__(self, data):
        try:
            self._grid = np.array(data, dtype=float)
        except ValueError:
            raise ValueError("Todas las filas de la matriz deben tener el mismo numero de columnas.")

    def getDimensions(self):
        return self._grid.shape

    def getElement(self, row, col):
        return self._grid[row, col]

    def setElement(self, row, col, value):
        self._grid[row, col] = value

    def getGrid(self):
        return self._grid.copy()

    def __str__(self):
        return str(self._grid)

class MatrixOperations:
    def add(self, matrixA, matrixB):
        pass

    def subtract(self, matrixA, matrixB):
        pass