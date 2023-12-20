# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        # Dictionary to store node values and their frequencies
        self.freq_map = {}
        self.traverse(root)

        # Find the maximum frequency
        max_freq = max(self.freq_map.values())

        # Get all values with maximum frequency
        modes = [key for key, value in self.freq_map.items() if value == max_freq]
        return modes

    def traverse(self, node):
        if not node:
            return

        # Update frequency map
        self.freq_map[node.val] = self.freq_map.get(node.val, 0) + 1

        # Traverse left and right subtrees
        self.traverse(node.left)
        self.traverse(node.right)