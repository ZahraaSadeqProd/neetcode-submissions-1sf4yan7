class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} # {difference sum needed : index}
        
        for i in range(len(nums)):

            if nums[i] in diff:
                return [diff[nums[i]], i]

            val = target - nums[i]
            diff[val] = i


        return [diff[val], len(nums) - 1]