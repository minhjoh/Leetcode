class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        num = max(candies)
        li = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= num:
                li.append(True)
            else:
                li.append(False)
        return li