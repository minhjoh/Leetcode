# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # A map to store all nodes by value
        nodes = {}
        
        # A set to keep track of all children nodes
        children = set()
        
        # Function to get the node for a given value, creating it if necessary
        def getNode(val):
            if val not in nodes:
                nodes[val] = TreeNode(val)
            return nodes[val]

        # Create the tree nodes and connections
        for parent_val, child_val, is_left in descriptions:
            parent = getNode(parent_val)
            child = getNode(child_val)
            if is_left:
                parent.left = child
            else:
                parent.right = child
            children.add(child_val)
        
        # The root is the one node that is not a child of any node
        root = None
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in children:
                root = getNode(parent_val)
                break
        
        return root



