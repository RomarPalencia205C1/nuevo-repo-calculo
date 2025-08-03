import numpy as np
from matrix.matrixOperations import Matrix

class LinearAlgebraService:
    def gaussJordan(self, matrix: Matrix):
        A = matrix.getGrid()
        rows, cols = matrix.getDimensions()

        for i in range(rows):
            pivot = A[i, i]
            if pivot == 0:
                raise ValueError("Elemento pivote es cero, el metodo no puede continuar.")
            
            A[i] = A[i] / pivot

            for j in range(rows):
                if i != j:
                    factor = A[j, i]
                    A[j] = A[j] - factor * A[i]
        
        return Matrix(A)

    def gaussianElimination(self, matrix: Matrix, pivot_strategy: str = 'parcial'):
        A = matrix.getGrid()
        rows, cols = matrix.getDimensions()

        for k in range(rows):
            self._applyPivoting(A, k, pivot_strategy)
            
            for i in range(k + 1, rows):
                factor = A[i, k] / A[k, k]
                A[i, k:] = A[i, k:] - factor * A[k, k:]
        
        return Matrix(A)

    def _applyPivoting(self, A: np.ndarray, k: int, strategy: str):
        rows, _ = A.shape
        if strategy == 'parcial':
            max_index = k + np.argmax(np.abs(A[k:, k]))
            A[[k, max_index]] = A[[max_index, k]] 
        elif strategy == 'completo':

            sub_matrix = A[k:, k:]
            max_val_in_sub = np.argmax(np.abs(sub_matrix))

            max_row_local, max_col_local = np.unravel_index(max_val_in_sub, sub_matrix.shape)
            max_row_global, max_col_global = k + max_row_local, k + max_col_local
            
            A[[k, max_row_global]] = A[[max_row_global, k]] 
            A[:, [k, max_col_global]] = A[:, [max_col_global, k]] 

        elif strategy != 'escalado':
            print(f"Advertencia: Estrategia de pivoteo '{strategy}' no reconocida. No se aplico pivoteo.")

    def getPossibleMatrixOperations(self, matrixA: Matrix, matrixB: Matrix):
        ops = []
        dimsA = matrixA.getDimensions()
        dimsB = matrixB.getDimensions()

        if dimsA == dimsB:
            ops.append("Suma")
            ops.append("Resta")
        
        if dimsA[1] == dimsB[0]:
            ops.append("Multiplicacion")
        
        return ops