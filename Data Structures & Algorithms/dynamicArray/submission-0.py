class DynamicArray:
    
    def __init__(self, capacity: int):
        self.validIndex = 0
        self.array = [0] * capacity


    def get(self, i: int) -> int:
        if i < self.validIndex:
            return self.array[i]


    def set(self, i: int, n: int) -> None:
        if i < self.validIndex:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.validIndex == len(self.array):
            self.resize();

        self.array[self.validIndex] = n
        self.validIndex += 1

    def popback(self) -> int:
        if not self.array:
            return -1
    
        self.validIndex = max(0, self.validIndex - 1)
        val = self.array[self.validIndex]
        
        return val 
 

    def resize(self) -> None:
        self.array = self.array + ([0] * len(self.array))


    def getSize(self) -> int:
        return self.validIndex
        
    
    def getCapacity(self) -> int:
        return len(self.array)
