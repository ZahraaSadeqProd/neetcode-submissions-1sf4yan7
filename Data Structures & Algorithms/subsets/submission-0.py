class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        self.dfs(nums, stack, res, 0)

        return res


    def dfs(self, nums, stack, res, i):

        if i >= len(nums):
            res.append(stack.copy())
            return

        # the left child is nums[i]
        stack.append(nums[i])
        self.dfs(nums, stack, res, i + 1)  

        # the right child is always the empty set
        stack.pop()
        self.dfs(nums, stack, res, i + 1)


        




