import re
from core.numericValue import NumericValue

class DecimalNumber(NumericValue):
    def _validate(self):
        pattern = r'^-?[0-9]+([,.][0-9]+)?$'
        return re.match(pattern, self.getRawValue()) is not None

    def _convertToNumber(self):
        return float(self.getRawValue().replace(',', '.'))

    def getNormalizedForm(self):
        return f"{self.getValue():.6e}"

    def countSignificantFigures(self):
        valueStr = self.getRawValue().replace(',', '.').lstrip('-')
        if '.' in valueStr:
            processedStr = valueStr.replace('.', '')
            if self.getValue() != 0 and abs(self.getValue()) < 1:
                return len(processedStr.lstrip('0'))
            return len(processedStr)
        return len(valueStr.rstrip('0')) if '.' not in valueStr else len(valueStr)

    def getPossibleOperations(self):
        return ["Suma", "Resta", "Multiplicacion", "Division"]