class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        [-2,4,-5,4,-5,9,4]
            i         j

        """
        currSumMax = 0
        maxSum = nums[0]

        currSumMin = 0
        minSum = nums[0]

        total = 0




        for n in nums:
            currSumMax = max(currSumMax + n, n)
            maxSum = max(currSumMax, maxSum)

            
            currSumMin = min(currSumMin + n, n)
            minSum = min(currSumMin, minSum)

            total += n

        
            
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum