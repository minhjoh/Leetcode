class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        heap = []
        for num, freq in freqs.items():
            heap.append([num, freq])
        
        heap.sort(reverse=True)

        res = []
        for num, freq in heap:
            res.append([num]*freq)
        
        def len_dict(e):
            return len(e)
        
        res.sort(key=len_dict)

        result = []
        for li in res:
            result += li
        return result
        

            
