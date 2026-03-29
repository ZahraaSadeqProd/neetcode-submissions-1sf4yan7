class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            else:
                nums[j] = nums[i]
                j += 1
                count += 1

        return count
