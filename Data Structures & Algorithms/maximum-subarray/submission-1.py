class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            currentSum = max(currentSum + n, n)
            maxSum = max(maxSum, currentSum)

        return maxSum