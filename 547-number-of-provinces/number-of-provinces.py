class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def Find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]
    
    def Unionbyrank(self, i, j):
        irep = self.Find(i)
        jrep = self.Find(j)

        irank = self.rank[irep]
        jrank = self.rank[jrep]
        if irep == jrep:
            return 0

        if irank <= jrank:
            self.parent[irep] = jrep
            self.rank[jrep] += 1
        elif jrank < irank: 
            self.parent[jrep] = irep 
            self.rank[irep] += 1
        return 1
            

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        ans = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    ans-=uf.Unionbyrank(i,j)

        return ans


        