class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minVal:
            self.minVal.append(min(self.minVal[-1], val))
        else:
            self.minVal.append(val)



    def pop(self) -> None:
        if self.stack: 
            self.minVal.pop()
            return self.stack.pop()
        return None 


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

        return None

    def getMin(self) -> int:
        if self.minVal:
            return self.minVal[-1]
        return None
