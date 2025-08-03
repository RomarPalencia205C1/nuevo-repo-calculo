from abc import ABC, abstractmethod

class NumericValue(ABC):
    def __init__(self, rawValue):
        self._rawValue = rawValue
        if not self._validate():
            raise ValueError(f"El valor '{rawValue}' no es valido.")
        self._value = self._convertToNumber()

    def getRawValue(self):
        return self._rawValue

    def getValue(self):
        return self._value

    @abstractmethod
    def _validate(self):
        pass

    @abstractmethod
    def _convertToNumber(self):
        pass

    @abstractmethod
    def getNormalizedForm(self):
        pass

    @abstractmethod
    def countSignificantFigures(self):
        pass

    @abstractmethod
    def getPossibleOperations(self):
        pass