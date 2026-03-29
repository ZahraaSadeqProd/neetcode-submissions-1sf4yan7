class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, color, image[sr][sc], set())
        return image
        
        
        
    def dfs(self, image, r, c, color, ogColor, visit):
        if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or image[r][c] == color or image[r][c] != ogColor:
            return 0
  
            
        image[r][c] = color


        visit.add((r, c))
        
        self.dfs(image, r + 1, c, color, ogColor, visit)
        self.dfs(image, r - 1, c, color, ogColor, visit)
        self.dfs(image, r, c + 1, color, ogColor, visit)
        self.dfs(image, r, c - 1, color, ogColor, visit)

        visit.remove((r, c))

        return 



