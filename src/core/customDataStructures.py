class CustomList:
    def __init__(self):
        self._size = 0
        self._capacity = 4
        self._elements = [None] * self._capacity

    def append(self, element):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._elements[self._size] = element
        self._size += 1

    def _resize(self, newCapacity):
        newArray = [None] * newCapacity
        for i in range(self._size):
            newArray[i] = self._elements[i]
        self._elements = newArray
        self._capacity = newCapacity

    def get(self, index):
        if not (0 <= index < self._size):
            raise IndexError("El indice de la lista esta fuera de rango.")
        return self._elements[index]

    def size(self):
        return self._size

    def __iter__(self):
        for i in range(self.size()):
            yield self.get(i)