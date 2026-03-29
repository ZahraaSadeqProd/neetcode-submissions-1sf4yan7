# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        queue = deque()
        queue.append(root)

        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                node = cur

                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)

                if i == length - 1:
                    res.append(node.val)

        return res[1:]