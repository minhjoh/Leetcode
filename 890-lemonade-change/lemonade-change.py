class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            elif bill == 20:
                if ten == 0:
                    five -= 3
                else:
                    ten -= 1
                    five -= 1
            if ten < 0 or five < 0:
                return False
        return True