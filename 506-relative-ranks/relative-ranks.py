import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        index_map = {score[i]: i for i in range(len(score))}
        
        heap = [(num, index) for num, index in index_map.items()]
        heapq.heapify(heap)
        
        medal_names = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        
        rank = len(score)
        result = [""] * len(score)
        while heap:
            num, index = heapq.heappop(heap)
            result[index] = medal_names.get(rank, str(rank))
            rank -= 1
        return result
