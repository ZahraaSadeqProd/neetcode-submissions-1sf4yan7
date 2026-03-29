class Node:
    def __init__(self, key, val):
        self.key  = key
        self.val  = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left = LRU and right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next  = self.right
        self.right.prev = self.left
        
    # remove node from list
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        next.prev = node

        node.prev = prev
        node.next = next


    def get(self, key: int) -> int:
        # if the key exists
        if key in self.cache:
            # remove it and add it to the right so its the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # then return the val
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        # if the key exists then remove it, 
        # we will update it with the new value and insert at the beginning
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if we exceeded the capacity then we remove the LRU from the left
        if len(self.cache) > self.cap:
            # remove node from list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
