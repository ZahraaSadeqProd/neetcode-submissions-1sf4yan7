class Solution:
    def dfs(self, i, j, rows, cols, obstacleGrid):
        if i >= rows or j >= cols or obstacleGrid[i][j] == 'x':
            return 0

        if obstacleGrid[i][j] > 0:
            return obstacleGrid[i][j]

        if i == rows - 1 and j == cols - 1:
            return 1

        obstacleGrid[i][j] = self.dfs(i + 1, j, rows, cols, obstacleGrid) + self.dfs(i, j + 1, rows, cols, obstacleGrid)
        return obstacleGrid[i][j]


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid) 
        cols = len(obstacleGrid[0])

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 'x'


        return self.dfs(0, 0, rows, cols, obstacleGrid)
