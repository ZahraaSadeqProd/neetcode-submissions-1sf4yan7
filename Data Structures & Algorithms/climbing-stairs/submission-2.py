class Solution:
    def climb(self, n: int, i: int, memo: {}) -> int:
        if i == n:
            return 1
        if i > n:
            return 0
        
        if i in memo:
            return memo[i]

        memo[i] = self.climb(n, i + 1, memo) + self.climb(n, i + 2, memo)
        return memo[i]

    def climbStairs(self, n: int) -> int:
        iterations = self.climb(n, 0, {})
        return iterations
