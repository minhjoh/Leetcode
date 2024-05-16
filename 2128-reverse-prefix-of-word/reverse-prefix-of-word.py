class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        found_ch = False
        
        for char in word:
            prefix += char
            if not found_ch and char == ch:
                prefix = prefix[::-1]
                found_ch = True
        
        return prefix + word[len(prefix):]
