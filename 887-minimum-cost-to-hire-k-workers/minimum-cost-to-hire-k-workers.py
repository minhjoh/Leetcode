class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        n = len(q)
        workers = sorted([(w[i] / q[i], q[i]) for i in range(n)])
        
        min_w = float('inf')
        total_q = 0
        max_heap = []

        for ratio, qual in workers:
            total_q += qual
            heapq.heappush(max_heap, -qual)  
            
            if len(max_heap) > k:
                total_q += heapq.heappop(max_heap)  
            if len(max_heap) == k:
                min_w = min(min_w, total_q * ratio)
        return min_w