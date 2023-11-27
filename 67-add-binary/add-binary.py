class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = str(int(a) + int(b))
        index = 0
        n = len(c)
        while n - 1 - index >= 0:
            if int(c[n - 1 - index]) == 2 or int(c[n - 1 - index]) == 3:
                c = str(int(c) + 8 * (10 ** index))
            index += 1
        return c