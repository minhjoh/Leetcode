class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        expected = []
        for i in range(len(heights)):
            expected.append(heights[i])
        expected.sort()
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count