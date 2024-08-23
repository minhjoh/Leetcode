class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern_to_word = {}
        word_to_pattern = {}
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in pattern_to_word:
                if pattern_to_word[pattern[i]] != words[i]:
                    return False
            else:
                pattern_to_word[pattern[i]] = words[i]
            
            if words[i] in word_to_pattern:
                if word_to_pattern[words[i]] != pattern[i]:
                    return False
            else:
                word_to_pattern[words[i]] = pattern[i]
        
        return True