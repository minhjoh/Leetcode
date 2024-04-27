import heapq
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        while k > 0:
            pile = heapq.heappop(heap)
            heapq.heappush(heap, pile//2)
            k -= 1
        return -sum(heap)