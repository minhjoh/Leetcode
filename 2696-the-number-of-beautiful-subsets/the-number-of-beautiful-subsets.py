class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start, subset):
            nonlocal count
            # Check if the current subset is beautiful
            if subset:
                count += 1                                      # O(n^2 * 2^n), O(n)
            
            for i in range(start, len(nums)):
                # Check if adding nums[i] would violate the beautiful condition
                if any(abs(nums[i] - num) == k for num in subset):
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        count = 0
        nums.sort() 
        backtrack(0, [])
        return count