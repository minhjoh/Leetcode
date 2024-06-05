class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            common_count &= word_count
        
        res = []
        for char, freq in common_count.items():
            res.extend([char] * freq)
        
        return res