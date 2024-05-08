class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        index_map = [[score[i], i] for i in range(len(score))]
        
        heapq.heapify(index_map)
        
        rank = len(score)
        while index_map:
            pos = heapq.heappop(index_map)
            if rank == 1:
                score[pos[1]] = "Gold Medal"
            elif rank == 2:
                score[pos[1]] = "Silver Medal"
            elif rank == 3:
                score[pos[1]] = "Bronze Medal"
            else:
                score[pos[1]] = str(rank)
            rank -= 1
        return score

        
