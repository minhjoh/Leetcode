class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {score[i]: i for i in range(len(score))}
        
        sorted_dic = sorted(dic.items(), reverse=True)
        
        for rank, (val, index) in enumerate(sorted_dic, 1):
            if rank == 1:
                val = "Gold Medal"
            elif rank == 2:
                val = "Silver Medal"
            elif rank == 3:
                val = "Bronze Medal"
            else:
                val = str(rank)
            score[index] = val
        
        return score