import os
import random
import numpy as np
from core.numericValue import NumericValue
from modules.errorCalculator import ErrorCalculator
from services.linearAlgebraService import LinearAlgebraService
from matrix.matrixOperations import Matrix

class ReportService:
    def __init__(self):
        self._error_calculator = ErrorCalculator()
        self._algebra_service = LinearAlgebraService()

    def generateFullReport(self, dataMatrix, original_filename: str):
        analysis_content = self._generateAnalysisContent(dataMatrix)
        error_content = self._generateErrorContent(dataMatrix)
        matrix_content = self._generateMatrixContent(dataMatrix)

        full_report_content = (
            f"{analysis_content}\n\n"
            "=== Resultados del analisis de errores ===\n"
            f"{error_content}\n\n"
            "=== Operaciones Matriciales ===\n"
            f"{matrix_content}"
        )

        self._saveReportToFile(full_report_content, original_filename)

    def _generateAnalysisContent(self, dataMatrix):
        content = ""
        for i, row in enumerate(dataMatrix):
            for j, item in enumerate(row):
                if isinstance(item, NumericValue):
                    content += (
                        f"Fila {i+1}, Col {j+1}: "
                        f"Valor: {item.getRawValue()} | "
                        f"Sistema: {type(item).__name__.replace('Number','')} | "
                        f"Normalizado: {item.getNormalizedForm()} | "
                        f"Digitos significativos: {item.countSignificantFigures()} | "
                        f"Operaciones: {', '.join(item.getPossibleOperations())}\n"
                    )
        return content

    def _generateErrorContent(self, dataMatrix):
        content = ""
        all_numbers = [item for row in dataMatrix for item in row if isinstance(item, NumericValue)]

        for i in range(len(all_numbers) - 1):
            val1, val2 = all_numbers[i], all_numbers[i+1]
            try:
                v1_float, v2_float = float(val1.getValue()), float(val2.getValue())
            except (ValueError, TypeError):
                continue

            content += f"Comparacion: {v1_float:.6f} vs {v2_float:.6f}\n"
            abs_error = self._error_calculator.calculateAbsoluteError(val1, val2)
            trunc_error = self._error_calculator.calculateTruncationError(val1)
            round_error = self._error_calculator.calculateRoundingError(val1)
            
            content += f" - Error Absoluto: {abs_error:.6f}\n"
            try:
                rel_error = self._error_calculator.calculateRelativeError(val1, val2)
                prop_error = self._error_calculator.calculatePropagationErrorSum(abs_error, rel_error)
                content += f" - Error Relativo: {rel_error:.6f}\n"
                content += f" - Error de Propagacion (Suma): {prop_error:.6f}\n"
            except ValueError:
                content += " - Error Relativo: inf\n"
                content += " - Error de Propagacion (Suma): inf\n"
            
            content += f" - Error por Redondeo: {round_error:.6f}\n"
            content += f" - Error por Truncamiento: {trunc_error:.6f}\n"
        
        return content
    
    def _generateMatrixContent(self, dataMatrix):
        content = ""
        try:
            matrix_object = self._createMatrixFromData(dataMatrix)
            if not matrix_object:
                return "No se pudo crear una matriz valida a partir de los datos.\n"
            content += "Matriz en Base 10:\n"
            content += str(matrix_object) + "\n\n"
            rows, cols = matrix_object.getDimensions()
            if rows == cols - 1:
                result_gauss_jordan = self._algebra_service.gaussJordan(matrix_object)
                content += "Resultado de Gauss-Jordan:\n"
                content += str(result_gauss_jordan) + "\n"
            else:
                content += "El archivo no contiene un sistema de ecuaciones valido para los metodos de Gauss.\n"
            return content
        except Exception as e:
            return f"Error durante las operaciones matriciales: {e}\n"

    def _createMatrixFromData(self, dataMatrix):
        numeric_data = []
        max_cols = 0
        for row in dataMatrix:
            if row.size() > max_cols: max_cols = row.size()
        for row in dataMatrix:
            row_data = [item.getValue() if isinstance(item, NumericValue) else 0.0 for item in row]
            while len(row_data) < max_cols: row_data.append(0.0)
            numeric_data.append(row_data)
        try:
            return Matrix(numeric_data)
        except ValueError:
            return None

    def _saveReportToFile(self, content: str, original_filename: str):
        report_directory = "resultados"
        os.makedirs(report_directory, exist_ok=True)
        
        # --- NUEVA MODIFICACION ---
        base_name = os.path.splitext(original_filename)[0]
        name_parts = base_name.split('_')
        
        # Generamos un nuevo serial aleatorio de 3 digitos.
        random_serial = f"{random.randint(100, 999):03d}"
        
        # Construimos el nuevo nombre del archivo.
        # Si el formato original es correcto (ej. 'nombre_fecha_serial'), lo respetamos.
        if len(name_parts) == 3:
            new_name = f"{name_parts[0]}_{name_parts[1]}_{random_serial}.txt"
        else:
            # Si no, usamos un formato por defecto.
            new_name = f"{base_name}_{random_serial}.txt"

        report_path = os.path.join(report_directory, new_name)

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nReporte guardado con exito en: {report_path}")