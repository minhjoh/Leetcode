# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(root,is_left):
            nonlocal s
            if not root:
                return
            if not root.left and not root.right and is_left:
                s += root.val
            left = dfs(root.left, True)
            right = dfs(root.right, False)
            
        dfs(root, False)
        return s
        
        
