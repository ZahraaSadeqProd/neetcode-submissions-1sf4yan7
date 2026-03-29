class MyStack:
    def __init__(self):
        self.queue = deque()
        self.topVal = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.topVal = x

    def pop(self) -> int:
        popped = 0
        length = len(self.queue)
        while length > 1:
            self.topVal = self.queue.popleft()
            self.queue.append(self.topVal)
            length -= 1
        popped = self.queue.popleft()
        return popped
        
    def top(self) -> int:
        return self.topVal

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()