class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = []
        for i in range(len(names)):
            h.append([heights[i], names[i]])
        
        h.sort(reverse=True)
        res = [name for height, name in h]
        return res
        
