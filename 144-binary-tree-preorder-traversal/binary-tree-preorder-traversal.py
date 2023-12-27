# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Preorder(root):
            if root is None:
                return
            li.append(root.val)
            Preorder(root.left)
            Preorder(root.right)
            
            return
        li = []
        Preorder(root)
        return li
        