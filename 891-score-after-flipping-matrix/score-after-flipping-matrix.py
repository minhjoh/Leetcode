class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            curr, curr_xor = "", ""
            for j in range(n):
                curr += str(grid[i][j])
                curr_xor += str(grid[i][j] ^ 1)
            if int(curr_xor) > int(curr):
                for j in range(n):
                    grid[i][j] ^= 1
        
        for i in range(n):
            col = 0
            for j in range(m):
                col += grid[j][i]

            if col <= m//2:
                for j in range(m):
                    grid[j][i] ^= 1
        
        result = 0
        for i in range(m):
            temp = ""
            for j in range(n):
                temp += str(grid[i][j])
            # print(int(temp,2), temp)
            result += int(temp,2)
        return result
            


