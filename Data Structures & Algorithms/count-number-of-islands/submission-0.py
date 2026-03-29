class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        numIslands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visit:
                    count = self.dfs(grid, r, c, visit)
                    if count > 0:
                        numIslands += 1

        return numIslands


    def dfs(self, grid, r, c, visit):
        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r, c) in visit or grid[r][c] == '0':
            return 0
        
        count = 0

        if grid[r][c] == '1':
            visit.add((r, c))
            count = 1
            

        




        count += self.dfs(grid, r + 1, c, visit)
        count += self.dfs(grid, r - 1, c, visit)
        count += self.dfs(grid, r, c + 1, visit)
        count += self.dfs(grid, r, c - 1, visit)
            

        return count 


