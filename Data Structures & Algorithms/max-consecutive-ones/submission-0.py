class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        local_count = 0

        for num in nums:
            if num == 1:
                local_count += 1
            else:
                local_count = 0

            max_consecutive = max(max_consecutive, local_count)


        return max_consecutive