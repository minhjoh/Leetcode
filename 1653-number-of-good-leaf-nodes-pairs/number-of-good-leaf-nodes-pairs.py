# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        path = [0]  # Sử dụng danh sách để lưu trữ kết quả

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # Khoảng cách đến lá hiện tại là 1
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Đếm các cặp lá giữa cây con trái và cây con phải
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        path[0] += 1

            # Trả về các khoảng cách được tăng thêm 1 (cho nút hiện tại)
            return [d + 1 for d in left_distances + right_distances]

        dfs(root)
        return path[0]

