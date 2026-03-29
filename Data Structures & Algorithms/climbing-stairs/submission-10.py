class Solution:

    def climbStairs(self, n: int) -> int:
        """
        dynamic programming

        way(2) = ways(0) + way(1)
               = 1 + 1 = 2

        """

        if n <= 1:
            return 1 

        n0 = n1 = 1
        sum = 1
        i = 2
        
        while i <= n:
            sum = n0 + n1

            n0 = n1
            n1 = sum 
            

            i += 1

        return sum


        