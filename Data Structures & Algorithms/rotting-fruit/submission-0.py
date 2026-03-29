class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = collections.deque()
        time, fresh = 0, 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    if (r + dr in range(ROWS) and 
                        c + dc in range(COLS) and 
                        grid[r + dr][c + dc] == 1):
                            grid[r + dr][c + dc] = 2
                            queue.append((r + dr, c + dc))
                            fresh -= 1
            time += 1
                                

        return time if fresh == 0 else -1