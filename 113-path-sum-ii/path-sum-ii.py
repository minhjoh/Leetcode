# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, node_sum, li):
            if not root:
                return True
            if root:
                node_sum += root.val
                li.append(root.val)
            if not root.left and not root.right and node_sum == targetSum:
                target_li.append(li[:])
                li.pop()
                return True
            left, right = dfs(root.left, node_sum, li), dfs(root.right, node_sum, li)
            li.pop()
        
        target_li = []
        dfs(root, 0, [])
        return target_li
