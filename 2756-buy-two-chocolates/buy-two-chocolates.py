class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        left = money - prices[0] - prices[1]
        if left >= 0:
            return left
        return money