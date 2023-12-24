class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        CountFor1 = CountFor0 = 0
        
        for i, char in enumerate(s):
            if i % 2 == 0:
                if char == '0':
                    CountFor1 += 1
                else:
                    CountFor0 += 1
            else:
                if char == '1':
                    CountFor1 += 1
                else:
                    CountFor0 += 1
        return min(CountFor1, CountFor0)