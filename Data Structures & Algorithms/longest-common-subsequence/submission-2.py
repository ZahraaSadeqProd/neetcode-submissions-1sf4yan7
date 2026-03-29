class Solution:
    """
       c a t
    c  3 0 0
    r  0 2 1
    a  0 2 1
    b  0 0 1
    t  0 0 1

    """
    def dfs(self, i, j, rows, cols, text1, text2, cache):
        if i >= rows or j >= cols:
            return 0

        if cache[i][j] > 0:
            return cache[i][j]

        if text1[i] == text2[j]:
            cache[i][j] = 1 + self.dfs(i + 1, j + 1, rows, cols, text1, text2, cache)
        else:
            cache[i][j] = max(self.dfs(i + 1, j, rows, cols, text1, text2, cache),
                                self.dfs(i, j + 1, rows, cols, text1, text2, cache))
        return cache[i][j]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        cache = [[0] * cols for i in range(rows)]

        self.dfs(0, 0, rows, cols, text1, text2, cache)
        print(cache)

        return self.dfs(0, 0, rows, cols, text1, text2, cache)

