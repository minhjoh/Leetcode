class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = {0: 1}
        current_sum = 0

        for num in nums:
            current_sum += num % 2
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1

        return count