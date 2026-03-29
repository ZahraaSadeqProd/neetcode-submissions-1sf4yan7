class Solution:
    def dfs(self, i, j, rows, cols, cache):
        if i == rows or j == cols:
            return 0
        
        if cache[i][j] > 0:
            return cache[i][j]

        if i == rows - 1 and j == cols - 1:
            return 1

        cache[i][j] = self.dfs(i + 1, j, rows, cols, cache) + self.dfs(i, j + 1, rows, cols, cache)
        return cache[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]

        return self.dfs(0, 0, m, n, cache)

        