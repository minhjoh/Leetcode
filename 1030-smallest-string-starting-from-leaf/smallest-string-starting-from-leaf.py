# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, string):
            if not root:
                return
            string += chr(root.val + 97) 
            if not root.left and not root.right:
                nonlocal smallest
                current_str = string[::-1]
                if smallest == "":
                    smallest = current_str
                else:
                    smallest = min(smallest, current_str)
                return
            dfs(root.left, string)
            dfs(root.right, string)
        smallest = ""
        dfs(root, "")
        return smallest


        
