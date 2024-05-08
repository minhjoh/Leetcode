class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-score[i], i) for i in range(len(score))]
        heapq.heapify(heap)
        
        rank_names = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        
        result = [""] * len(score)
        rank = 0
        while heap:
            _, index = heapq.heappop(heap)
            result[index] = rank_names.get(rank, str(rank + 1))
            rank += 1
        return result