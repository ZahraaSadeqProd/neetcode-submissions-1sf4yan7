class Solution:
    def dfs(self, i, j, rows, cols, obstacleGrid):
        if i >= rows or j >= cols:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        if i == rows - 1 and j == cols - 1:
            return 1

        if obstacleGrid[i][j] < 0:
            return -obstacleGrid[i][j]

        paths = self.dfs(i + 1, j, rows, cols, obstacleGrid) + \
                self.dfs(i, j + 1, rows, cols, obstacleGrid)

        obstacleGrid[i][j] = -paths
        return paths

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        return self.dfs(0, 0, rows, cols, obstacleGrid)