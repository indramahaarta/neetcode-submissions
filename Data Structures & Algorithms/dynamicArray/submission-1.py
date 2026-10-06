class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0]*capacity
        self.size = 0
        # print(self.arr)

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.arr):
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        res = self.arr[self.size-1]
        self.size -= 1
        return res

    def resize(self) -> None:
        self.arr.extend([0]*self.size)

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return len(self.arr)