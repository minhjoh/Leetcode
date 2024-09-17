class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordDic = {}
        res = []
        for word1 in s1.split():
            wordDic[word1] = wordDic.get(word1, 0) + 1
        for word2 in s2.split():
            wordDic[word2] = wordDic.get(word2, 0) + 1
        for word, freq in wordDic.items():
            if freq == 1:
                res.append(word)
        return res