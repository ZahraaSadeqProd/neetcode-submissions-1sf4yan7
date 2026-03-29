class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i] 
                if diff > maxP:
                    maxP = diff
        return maxP