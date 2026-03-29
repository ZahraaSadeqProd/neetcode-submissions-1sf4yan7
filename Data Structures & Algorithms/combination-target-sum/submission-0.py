class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        self.dfs(nums, stack, res, target, 0, 0)

        return res


    def dfs(self, nums, stack, res, target, total, i):
        if total == target:
            res.append(stack.copy())
            return
        
        if i >= len(nums) or total > target:
            return

        # the left child is nums[i]
        stack.append(nums[i])
        self.dfs(nums, stack, res, target, total + nums[i], i)  

        # the right child is always the empty set
        stack.pop()
        self.dfs(nums, stack, res, target, total, i + 1)


        




