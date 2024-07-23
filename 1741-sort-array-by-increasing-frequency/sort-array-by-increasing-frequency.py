class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        sort_by_num = []
        for num, freq in freqs.items():
            sort_by_num.append([num, freq])
        
        sort_by_num.sort(reverse=True)

        sort_by_freq = []
        for num, freq in sort_by_num:
            sort_by_freq.append([num]*freq)
        
        def len_dict(e):
            return len(e)
        
        sort_by_freq.sort(key=len_dict)

        res = []
        for li in sort_by_freq:
            res += li

        return res
        

            
