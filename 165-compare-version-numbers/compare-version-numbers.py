class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        n1, n2 = len(v1), len(v2)
        i, j = 0, 0
        
        while i < n1 or j < n2:
            num1 = v1[i] if i < n1 else 0
            num2 = v2[j] if j < n2 else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            
            i += 1
            j += 1
        
        return 0