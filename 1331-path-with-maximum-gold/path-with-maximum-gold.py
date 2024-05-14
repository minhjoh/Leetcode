class Solution:
    def dfs(self, grid, count, i, j, maxGold):
        x = [1, -1, 0, 0]  
        y = [0, 0, -1, 1]  

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return maxGold

        if grid[i][j]:
            cur = grid[i][j]
            count += cur
            grid[i][j] = 0

            maxGold = max(maxGold, count)
            for k in range(4):
                newX = i + x[k]
                newY = j + y[k]

                maxGold = self.dfs(grid, count, newX, newY, maxGold)
            grid[i][j] = cur
        
        return maxGold

    def getMaximumGold(self, grid):
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    maxGold = self.dfs(grid, 0, i, j, maxGold)

        return maxGold
