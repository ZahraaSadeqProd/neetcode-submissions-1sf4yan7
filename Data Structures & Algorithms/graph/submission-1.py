class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if dst not in self.graph:
            self.graph[dst] = set()
        if src not in self.graph:
            self.graph[src] = set()
        
        self.graph[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False

        if dst in self.graph[src]:
            self.graph[src].remove(dst)

            return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        queue = collections.deque()
        visit.add(src)
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True
                
                for neighbor in self.graph[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)

        return False
        

