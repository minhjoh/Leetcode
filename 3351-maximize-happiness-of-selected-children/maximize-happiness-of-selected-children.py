import heapq

class Solution:
    def maximumHappinessSum(self, happiness, k):
        heap = [-x for x in happiness]  
        heapq.heapify(heap)
        
        sum_happy = 0
        for i in range(k):
            max_happiness = -heapq.heappop(heap)  
            sum_happy += max(max_happiness - i, 0)
        
        return sum_happy