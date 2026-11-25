# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not q:
            return False

        if (p and q) and p.val == q.val:
            res1 = self.isSameTree(p.left, q.left)
            res2 = self.isSameTree(p.right, q.right)
            if res1 and res2:
                return True
        return False