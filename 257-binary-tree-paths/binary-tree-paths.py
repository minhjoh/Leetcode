# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(root, string):
            if root:
                string += str(root.val)
                if not root.left and not root.right:
                    res.append(string)
                else:
                    string += '->'
                    backtrack(root.left, string)
                    backtrack(root.right, string)

        res = []
        backtrack(root, "")
        return res
