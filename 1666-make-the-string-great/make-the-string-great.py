class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = True
        while flag:
            flag = False
            i = 0
            while i < len(s) - 1:
                try:
                    if ord(s[i]) == ord(s[i+1]) + 32 or ord(s[i]) == ord(s[i+1]) - 32:
                        s = s[:i] + s[i+2:]
                        flag = True
                    else:
                        i += 1
                except IndexError:
                    pass
        return s