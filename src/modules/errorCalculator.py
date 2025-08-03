class ErrorCalculator:
    # Determinar Error absoluto
    def calculateAbsoluteError(self, realValue, approximateValue):
        return abs(realValue.getValue() - approximateValue.getValue())

    # Determinar Error Relativo
    def calculateRelativeError(self, realValue, approximateValue):
        real = realValue.getValue()
        if real == 0:
            raise ValueError("El valor real no puede ser cero para el error relativo.")
        absoluteError = self.calculateAbsoluteError(realValue, approximateValue)
        return absoluteError / abs(real)

    # Determinar Error por redondeo
    def calculateRoundingError(self, number, decimalPlaces=0):
        original = number.getValue()
        rounded = round(original, decimalPlaces)
        return abs(original - rounded)

    # Determinar Error por truncamiento
    def calculateTruncationError(self, number, decimalPlaces=2):
        original = number.getValue()
        factor = 10 ** decimalPlaces
        truncated = int(original * factor) / factor
        return abs(original - truncated)
        
    # --- NUEVA MODIFICACION ---
    # Determinar Error por propagacion
    def calculatePropagationErrorSum(self, absolute_error: float, relative_error: float):
        # Basado en el formato del archivo de salida de ejemplo
        return absolute_error + relative_error