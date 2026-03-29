class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = float("inf")

    def push(self, val: int) -> None:            
        print(self.stack)
        if self.stack == []:
            self.stack.append(val)
            self.minVal = val
        else:
            if val <= self.minVal:
                self.stack.append(self.minVal)
                self.stack.append(val)
                self.minVal = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        print(self.stack)
        if self.stack: 
            pop = self.stack.pop()
            if pop == self.minVal and len(self.stack) != 0:
                prev_min = self.stack.pop()
                self.minVal = prev_min
            return pop
        return None 


    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            return top

        return None

    def getMin(self) -> int:
        if self.minVal != float("inf"):
            return self.minVal
        return None
