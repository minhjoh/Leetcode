class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_money = 0
        money_put = 1
        while n > 0:
            for i in range(7):
                sum_money = sum_money + i + money_put
                n -= 1
                if n == 0:
                    break
            money_put += 1
        return sum_money
            