class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        sub_islands = 0 

        def flood(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid2[i][j] == 0:
                return True
            
            if grid1[i][j] == 0:
                return False

            grid2[i][j] = 0
            
            up = flood(i - 1, j)
            down = flood(i + 1, j)
            left = flood(i, j - 1)
            right = flood(i, j + 1)
            
            # Return whether all parts of this island in grid2 are in grid1
            return up and down and left and right

        n, m = len(grid1), len(grid1[0])

        # Iterate over all cells in grid2 to find sub-islands
        for i in range(n):
            for j in range(m):
                # Start a new flood fill if we find a land cell in grid2
                if grid2[i][j] == 1:
                    # Check if all parts of this island in grid2 are sub-islands in grid1
                    if flood(i, j):
                        sub_islands += 1

        return sub_islands