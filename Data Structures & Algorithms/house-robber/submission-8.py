class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Problem:
        Input:
           - int array nums where nums[i] is the monet in the ith house

        Constraints:
           - cannot rob two adjacent houses

        Return
           - max money you can rob

        """

        """
        Approach:
        decision to make at each house
            - Rob it  -> skip next one
            - Skip it -> rob next one

        Brute force o(n^2)
        rob(i) = max(
            nums[i] + rob(i+2)  # take i -> skip next
            rob(i+1)            # skip i -> take next
        )

        DP
        for each house i:
            skip house i: then best total so far is dp[i-1]
            rob house  i: then best total so far is dp[i-2] + nums[i]


        """

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [0, 0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            #tmp = dp[1]
            dp[1], dp[0] = max(dp[1], dp[0] + nums[i]), dp[1]
            #dp[0] = tmp
            

        return dp[1] 






