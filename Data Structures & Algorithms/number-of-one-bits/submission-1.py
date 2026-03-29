class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            print("{0:b}".format(n))
            n = n >> 1

        return count
        