class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        sorted_nums = sorted(nums, key=lambda x: (freqs[x], -x))
        
        return sorted_nums
