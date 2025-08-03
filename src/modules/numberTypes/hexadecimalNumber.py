import re
from core.numericValue import NumericValue

class HexadecimalNumber(NumericValue):
    def _validate(self):
        return re.match(r'^[0-9a-fA-F]+$', self.getRawValue()) is not None

    def _convertToNumber(self):
        return int(self.getRawValue(), 16)

    def getNormalizedForm(self):
        return self.getRawValue().upper()

    def countSignificantFigures(self):
        return len(self.getRawValue())

    def getPossibleOperations(self):
        return ["Suma", "Resta", "Multiplicacion"]