# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs_check(root, sum_node, li):
            if not root:
                return 0
            if root:
                sum_node += root.val
            if not root.left and not root.right:
                li.append(sum_node)
            left, right = dfs_check(root.left, sum_node, li), dfs_check(root.right, sum_node, li)

        
        sum_node = 0
        li = []
        dfs_check(root, sum_node, li)
        if targetSum in li:
            return True
        return False
