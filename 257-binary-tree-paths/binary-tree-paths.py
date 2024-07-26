# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = [(root, f"{root.val}")]

        while stack:
            node, path = stack.pop()
            
            # Nếu là lá thì thêm đường đi vào kết quả
            if not node.left and not node.right:
                res.append(path)
            
            # Nếu có nhánh phải thì thêm vào stack
            if node.right:
                stack.append((node.right, f"{path}->{node.right.val}"))
            
            # Nếu có nhánh trái thì thêm vào stack
            if node.left:
                stack.append((node.left, f"{path}->{node.left.val}"))
        
        return res
