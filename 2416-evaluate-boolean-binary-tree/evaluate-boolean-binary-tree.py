# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == 1 or root.val == 0:
            return root.val
        ans = True
        if root.val == 2:
            ans = self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            ans = self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return ans
            