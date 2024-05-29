class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        num = int(s, 2)
        
        while num > 1:
            if num % 2 != 0:  
                num += 1
            else:  
                num //= 2
            step += 1
        
        return step

