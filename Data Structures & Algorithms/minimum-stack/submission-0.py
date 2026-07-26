class MinStack:

    def __init__(self):
        self.arr = []
        self.mn = [float('inf')]
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.mn.append(min(val, self.mn[-1]))


    def pop(self) -> None:
        self.arr.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.mn[-1]
        
