# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        return self.dfs(root)

    def dfs(self, p):
        if not p:
            return True
        if not self.dfs(p.left):
            return False
        if p.val <= self.prev:
            return False
        self.prev = p.val
        return self.dfs(p.right)