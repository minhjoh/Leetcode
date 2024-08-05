class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = {}
        for char in arr:
            freqs[char] = freqs.get(char, 0) + 1
        
        for char, freq in freqs.items():
            if freq == 1:
                k -= 1
            if k == 0:
                return char
        
        return ""