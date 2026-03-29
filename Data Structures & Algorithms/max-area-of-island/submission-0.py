class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxVal = 0



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = self.dfs(grid, r, c, visit)
                    maxVal = max(count, maxVal)


        return maxVal


    def dfs(self, grid, r, c, visit):
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r, c) in visit or grid[r][c] == 0:
            return 0


        visit.add((r, c))

        count = 1
        count += self.dfs(grid, r + 1, c, visit)
        count += self.dfs(grid, r - 1, c, visit)
        count += self.dfs(grid, r, c + 1, visit)
        count += self.dfs(grid, r, c - 1, visit)


        return count 



        