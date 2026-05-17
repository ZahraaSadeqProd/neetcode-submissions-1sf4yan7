class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        nums = [-1] 

        for i in range(len(arr) - 2, -1, -1):
            nums.append(max(nums[-1], arr[i + 1]))


        nums.reverse()

        # nums = nums[1:]
        # nums.append(-1)


        return nums
