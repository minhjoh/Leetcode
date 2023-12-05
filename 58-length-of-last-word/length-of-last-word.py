class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        n = len(word[len(word)-1])
        return n