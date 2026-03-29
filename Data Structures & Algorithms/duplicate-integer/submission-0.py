class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occur = {}

        for num in nums:
            if num in occur:
                return True
            occur[num] = 1
            
        return False