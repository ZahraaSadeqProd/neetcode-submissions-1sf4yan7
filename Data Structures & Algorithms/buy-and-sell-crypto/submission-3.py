class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxP = 0

        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i] 
        #         if diff > maxP:
        #             maxP = diff
        # return maxP

        L, maxProf = 0, 0

        for R in range(0, len(prices)):

            if prices[R] < prices[L]:
                L = R
            else:
                maxProf = max(maxProf, prices[R] - prices[L])
            R += 1

        
        return maxProf