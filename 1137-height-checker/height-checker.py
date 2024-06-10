class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_copy = heights[:]
        heights_copy.sort()
        count = 0
        for i in range(len(heights)):
            if heights_copy[i] != heights[i]:
                count += 1
        return count