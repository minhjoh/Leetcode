class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pre_xor = [0] * n
        for i in range(n):
            if i == 0:
                pre_xor[i] = arr[i]
            else:
                pre_xor[i] = arr[i] ^ pre_xor[i-1]

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if pre_xor[j] ^ pre_xor[i] == arr[i]:
                    ans += j - i
        return ans