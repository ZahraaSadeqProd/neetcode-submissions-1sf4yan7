class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for n in range(numCourses):
            graph[n] = []

        for courses in prerequisites:
            dst, src = courses # we can think of a as dst and b as src

            if src not in graph or dst not in graph:
                return False

            graph[src].append(dst)



        def dfs(node, neighbors):
            if node in visit:
                return False

            if neighbors == []:
                return True

            visit.add(node)
            for neighbor in neighbors:
                if not dfs(neighbor, graph[neighbor]):
                    return False
            
            return True


        for n in range(numCourses):
            visit = set()
            if not dfs(n, graph[n]):
                return False



        return True

