class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def merge(nums, l, m, r):
            n1 = m - l + 1
            n2 = r - m
        
            # create temp arrays
            L = [0] * (n1)
            R = [0] * (n2)
        
            # Copy data to temp arrays L[] and R[]
            for i in range(0, n1):
                L[i] = nums[l + i]
        
            for j in range(0, n2):
                R[j] = nums[m + 1 + j]
        
            # Merge the temp arrays back into arr[l..r]
            i = 0     # Initial index of first subarray
            j = 0     # Initial index of second subarray
            k = l     # Initial index of merged subarray
        
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
        
            # Copy the remaining elements of L[], if there
            # are any
            while i < n1:
                nums[k] = L[i]
                i += 1
                k += 1
        
            # Copy the remaining elements of R[], if there
            # are any
            while j < n2:
                nums[k] = R[j]
                j += 1
                k += 1
        
        # l is for left index and r is right index of the
        # sub-array of arr to be sorted
        
        
        def mergeSort(nums, l, r):
            if l < r:
        
                # Same as (l+r)//2, but avoids overflow for
                # large l and h
                m = l+(r-l)//2
        
                # Sort first and second halves
                mergeSort(nums, l, m)
                mergeSort(nums, m+1, r)
                merge(nums, l, m, r)
        
        n = len(nums)
        mergeSort(nums, 0, n-1)
        return nums[-k]
        