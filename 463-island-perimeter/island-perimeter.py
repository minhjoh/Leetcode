class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal sum_land
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == -1:
                return 
            if grid[i][j] == 1:
                if (i == 0 or grid[i - 1][j] == 0):
                    sum_land += 1
                if (i == len(grid) - 1 or grid[i + 1][j] == 0):
                    sum_land += 1
                if (j == 0 or grid[i][j - 1] == 0):
                    sum_land += 1
                if (j == len(grid[0]) - 1 or grid[i][j + 1] == 0):
                    sum_land += 1
                grid[i][j] = -1  # Mark visited land equal -1
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
                    
        sum_land = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        return sum_land
            


