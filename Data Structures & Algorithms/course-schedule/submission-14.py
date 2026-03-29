class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        if not prerequisites:
            return True

        for n in range(numCourses):
            graph[n] = []

        for dst, src in prerequisites:
            graph[src].append(dst)

        visit = set()

        def dfs(course):
            if course in visit:
                return False

            if graph[course] == []:
                return True

            visit.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            
            visit.remove(course)
            graph[course] = []

            return True

        for course in graph:
            if not dfs(course):
                return False

        return True

