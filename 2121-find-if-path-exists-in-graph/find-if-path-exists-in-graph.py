class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[jrep] = irep

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        n = len(range(n))
        unionfind = UnionFind(n)
        for i, j in edges:
            unionfind.union(i, j)
        return unionfind.find(source) == unionfind.find(destination)
    

    
        
