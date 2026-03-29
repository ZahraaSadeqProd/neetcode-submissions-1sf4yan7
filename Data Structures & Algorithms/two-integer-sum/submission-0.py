class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffSum = {}
        for i in range(0, len(nums)):
            if nums[i] in diffSum:
                return [diffSum[nums[i]], i]
            diffSum[target-nums[i]] = i

