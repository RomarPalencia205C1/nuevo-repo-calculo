class ErrorCalculator:
    def calculateAbsoluteError(self, realValue, approximateValue):
        return abs(realValue.getValue() - approximateValue.getValue())

    def calculateRelativeError(self, realValue, approximateValue):
        real = realValue.getValue()
        if real == 0:
            raise ValueError("El valor real no puede ser cero para el error relativo.")
        absoluteError = self.calculateAbsoluteError(realValue, approximateValue)
        return absoluteError / abs(real)

    def calculateRoundingError(self, number, decimalPlaces=0):
        original = number.getValue()
        rounded = round(original, decimalPlaces)
        return abs(original - rounded)

    def calculateTruncationError(self, number, decimalPlaces=2):
        original = number.getValue()
        factor = 10 ** decimalPlaces
        truncated = int(original * factor) / factor
        return abs(original - truncated)