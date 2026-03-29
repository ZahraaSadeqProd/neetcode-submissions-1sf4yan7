class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Its a Fibonacci sequence

        can climb with 1 or 2 steps until n

        return:
            num distinct ways to get to n

        
        e.g. n = 7

        1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
        2 + 1 + 1 + 1 + 1 + 1 = 7
        2 + 2 + 1 + 1 + 1 = 7
        2 + 2 + 2 + 1 = 7
        1 + 2 + 2 + 2 = 7
        1 + 1 + 1 + 2 + 2 = 7
        1 + 1 + 1 + 1 + 1 + 2 = 7
        1 + 2 + 1 + 1 + 1 + 1 = 7
        etc

        so we are starting from the base which is 
        1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
        then adding 2s each time 

        well adding a 2 and remove 2 ones
        so 
        2 + 1 + 1 + 1 + 1 + 1 = 7
        then moving that two until the end
        so we have now 6 combs of where we can put that two
        
        """



        dp = [0, 1]

        for i in range(0,  n):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp




        return dp[1]




































