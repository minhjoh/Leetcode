class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort()
        sum_happy = 0
        for i in range(k):
            sum_happy += max(happiness.pop() - i, 0)
        return sum_happy 