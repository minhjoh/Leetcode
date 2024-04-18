# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(root, height):
            if not root:
                return

            if depth==height+1:
                #adding to root.left
                temp = root.left
                root.left = TreeNode(val)
                root.left.left = temp
                
                # adding to root.right
                temp = root.right
                root.right = TreeNode(val)
                root.right.right = temp
                return root

            dfs(root.left, height+1)
            dfs(root.right, height+1)
            return root
        
        if depth == 1:
            new_root = TreeNode(val, root, None)
            return new_root
        dfs(root, 1)
        return root
        