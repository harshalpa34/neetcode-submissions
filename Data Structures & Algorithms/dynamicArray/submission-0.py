class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arrLen = 0  # Starts with 0 actual elements
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        # Changed to i >= 0. Checks against current length, not capacity.
        if 0 <= i < self.arrLen:
            return self.array[i]
        raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        # Changed to i >= 0
        if 0 <= i < self.arrLen:
            self.array[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n: int) -> None:
        # If capacity is full, double the size first
        if self.arrLen == self.capacity:
            self.resize()
            
        # Insert at the next empty slot
        self.array[self.arrLen] = n
        self.arrLen += 1

    def popback(self) -> int:
        if self.arrLen > 0:
            self.arrLen -= 1
            return self.array[self.arrLen]
        raise IndexError("Cannot pop from empty array")

    def resize(self) -> None:
        # Double the capacity
        self.capacity = self.capacity * 2
        # Fixed typo: used self.capacity instead of self.arrayLen
        self.array = self.array + [0] * (self.capacity - len(self.array))

    def getSize(self) -> int:
        return self.arrLen
    
    def getCapacity(self) -> int:
        return self.capacity