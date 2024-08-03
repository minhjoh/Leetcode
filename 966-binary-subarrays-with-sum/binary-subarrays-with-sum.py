class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        pSum = 0
        sum_counts = {0 : 1}

        for num in nums:
            pSum += num
            if pSum - goal in sum_counts:
                count += sum_counts[pSum - goal]
            sum_counts[pSum] = sum_counts.get(pSum, 0) + 1
        return count