class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {score[i]: i for i in range(len(score))}
        
        heap = []
        for num, index in dic.items():
            heapq.heappush(heap, (num, index))
        
        rank = len(score)
        while heap:
            pos = heapq.heappop(heap)
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

        
