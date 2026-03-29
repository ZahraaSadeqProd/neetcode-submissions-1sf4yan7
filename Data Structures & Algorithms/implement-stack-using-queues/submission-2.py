class MyStack:
    """
    stack = [3 2 5 1]
                   ^

    queue1 = [3 2 5 1]
              ^
    queue2 = [3 2 5 1]
                    ^

    then everytime i push or pop i switch between them
    


    """

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.queue = 1
        self.topVal = 0


    def push(self, x: int) -> None:
        if self.queue == 1:
             self.q1.append(x)
        else:
             self.q2.append(x)
        self.topVal = x

    def pop(self) -> int:
        popped = 0
        if self.queue == 1:
            while len(self.q1) > 1:
                self.topVal = self.q1.popleft()
                self.q2.append(self.topVal)
            popped = self.q1.popleft()
            self.queue = 2    
            return popped
        
        else:
            while len(self.q2) > 1:
                self.topVal = self.q2.popleft()
                self.q1.append(self.topVal)
            popped = self.q2.popleft()
            self.queue = 1    
            return popped


    def top(self) -> int:
        return self.topVal


    def empty(self) -> bool:
        if self.q1 or self.q2:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()