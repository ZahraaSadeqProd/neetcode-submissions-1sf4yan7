# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k, val = self.kth(root, k, 0)
        return val


    def kth(self, root, k, val):

        if not root:
            return k, val

        k, val = self.kth(root.left, k, val)
        
        k -= 1

        if k == 0:
            print(root.val)
            val = root.val
        k, val = self.kth(root.right, k, val)
            
        return k, val
