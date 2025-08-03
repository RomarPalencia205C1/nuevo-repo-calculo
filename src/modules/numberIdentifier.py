from modules.numberTypes.decimalNumber import DecimalNumber
from modules.numberTypes.binaryNumber import BinaryNumber
from modules.numberTypes.hexadecimalNumber import HexadecimalNumber

class NumberIdentifier:
    def identify(self, valueStr):
        try:
            if any(c in 'abcdef' for c in valueStr.lower()):
                return HexadecimalNumber(valueStr)
        except (ValueError, TypeError):
            pass

        try:
            return BinaryNumber(valueStr)
        except (ValueError, TypeError):
            pass
        
        try:
            return DecimalNumber(valueStr)
        except (ValueError, TypeError):
            pass

        return valueStr