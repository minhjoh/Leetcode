class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        def largest_value(grid, i, j):
            max_value = 0
            for row in range(3):
                for col in range(3):
                    max_value = max(max_value, grid[i+row][j+col])
            return max_value

        generated_matrix = [[0] * (n-2) for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                generated_matrix[i][j] = largest_value(grid, i, j)
        
        return generated_matrix
