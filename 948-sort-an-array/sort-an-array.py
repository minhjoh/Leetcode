class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, 0, n-1)
        return nums

    
    def merge(self, nums, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = nums[l + i]
    
        for j in range(0, n2):
            R[j] = nums[m + 1 + j]
    
        i = 0     
        j = 0     
        k = l     
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1
    
    def mergeSort(self, nums, l, r):
        if l < r:

            m = l+(r-l)//2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m+1, r)
            self.merge(nums, l, m, r)

    