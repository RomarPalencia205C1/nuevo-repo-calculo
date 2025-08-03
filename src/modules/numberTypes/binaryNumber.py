import re
from core.numericValue import NumericValue

class BinaryNumber(NumericValue):
    def _validate(self):
        return re.match(r'^(0b)?[01]+$', self.getRawValue()) is not None

    def _convertToNumber(self):
        value_to_convert = self.getRawValue().replace('0b', '')
        return int(value_to_convert, 2)

    def getNormalizedForm(self):
        return self.getRawValue()

    def countSignificantFigures(self):
        value_to_count = self.getRawValue().replace('0b', '')
        return len(value_to_count.lstrip('0')) or 1

    def getPossibleOperations(self):
        return ["Suma", "Resta", "Multiplicacion", "AND", "OR", "XOR"]