class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = {}
        computer = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    # story the column and row in 1 dimension
                    computer.append((i, j + m))

        def find(x):
            if x not in uf:
                uf[x] = x
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            uf[root_x] = root_y

        for x, y in computer:
            union(x, y)
        
        counter = collections.Counter([find(i) for i, _ in computer])
        return sum([i if i > 1 else 0 for i in counter.values()])

        

        
