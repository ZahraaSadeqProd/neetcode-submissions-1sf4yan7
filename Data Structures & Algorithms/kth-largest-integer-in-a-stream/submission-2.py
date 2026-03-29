
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        
        if not nums:
            return None

        # heapify
        self.heap += nums
        cur = (len(self.heap) - 1) // 2 # getting the first parent from the back

        while cur > 0:
            i = cur
            
            self.percolate(i)

            cur -= 1

        while len(self.heap) - 1 > self.k:
            self.pop(1)




    def percolate(self, i):
        while(2 * i) < len(self.heap):
            # if we have a right child
            # the right child val is less than the left child
            # parent val is bigger than right child
            if(2 * i + 1 < len(self.heap)) and (self.heap[2 * i + 1] < self.heap[2 * i]) and (self.heap[i] > self.heap[2 * i + 1]):
                self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                i = i * 2 + 1
            elif(self.heap[i] > self.heap[2 * i]): # else if the left child value is less than the parent
                self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]
                i = i * 2
            else:
                break

    def pop(self, i):
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1

        self.percolate(1)
        
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2


    def add(self, val: int) -> int:
        self.push(val)

        while len(self.heap) - 1 > self.k:
            self.pop(1)

        return self.heap[1]


