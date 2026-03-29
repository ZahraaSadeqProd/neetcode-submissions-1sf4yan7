class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            top = self.stack[-1]
            minVal = min(val, top[0])
            self.stack.append((minVal , val))

    def pop(self) -> None:
        if self.stack: 
            pop = self.stack.pop()
            return pop[1]
        return None 


    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            return top[1]

        return None

    def getMin(self) -> int:
        if self.stack:
            minVal = self.stack[-1]
            return minVal[0]
        return None
