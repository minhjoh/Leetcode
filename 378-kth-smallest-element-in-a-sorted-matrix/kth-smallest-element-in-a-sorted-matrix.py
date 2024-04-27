import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elements = len(matrix) * len(matrix)
        heap = []
        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)
        while k > 0:
            num = heapq.heappop(heap)
            k -= 1
        return num
        