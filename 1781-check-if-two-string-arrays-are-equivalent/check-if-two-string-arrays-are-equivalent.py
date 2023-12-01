class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 = str2 = str()
        for i in range(len(word1)):
            str1 = str1 + word1[i]
        for i in range(len(word2)):
            str2 = str2 + word2[i]
        if str1 == str2:
            return True
        else:
            return False