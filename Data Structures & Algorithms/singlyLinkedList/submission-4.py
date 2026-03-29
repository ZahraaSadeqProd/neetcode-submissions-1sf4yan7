class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = Node(0)


    def get(self, index: int) -> int:
        cur = self.head.next

        if cur is None:
            return -1

        while cur.next and index > 0:
            cur = cur.next
            index -= 1

        if index > 0:
            return -1
            
        return cur.val
        

    def insertHead(self, val: int) -> None:
        cur = self.head.next
        self.head.next = Node(val, cur)


    def insertTail(self, val: int) -> None:
        prev = self.head 
        cur = prev.next
        
        while cur:
            prev = cur
            cur = cur.next

        prev.next = Node(val)
        

    def remove(self, index: int) -> bool:
        prev = self.head
        cur = prev.next

        if cur is None:
            return False

        while cur.next and index > 0:
            prev = cur
            cur = cur.next
            index -= 1

        if index > 0:
            return False

        prev.next = cur.next
            
        return True


    def getValues(self) -> List[int]:
        arr = []
        cur = self.head.next

        while cur:
            arr.append(cur.val)
            cur = cur.next

        return arr
