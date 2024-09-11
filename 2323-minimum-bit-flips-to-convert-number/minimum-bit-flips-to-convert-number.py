class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        steps = 0
        tranStart = self.transform(start)
        tranGoal = self.transform(goal)
        n = len(tranStart) - len(tranGoal)
        if n > 0:
            tranGoal = "0" * n + tranGoal
        elif n < 0:
            tranStart = "0" * -n + tranStart
        for i in range(len(tranStart)):
            if tranStart[i] != tranGoal[i]:
                steps += 1
        return steps
    
    def transform(self, num):
        transNum = ""
        while num > 0:
            transNum += str(num % 2)
            num = num // 2
        return transNum[::-1]