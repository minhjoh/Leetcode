# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left and not root.right:
            return 0

        left_moves = self.distributeCoins(root.left)
        right_moves = self.distributeCoins(root.right)
        
        left_diff = root.left.val - 1 if root.left else 0
        right_diff = root.right.val - 1 if root.right else 0

        moves = abs(left_diff) + abs(right_diff)
        root.val += left_diff + right_diff
        moves += left_moves + right_moves

        return moves