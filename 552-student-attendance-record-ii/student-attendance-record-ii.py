class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9) + 7

        @cache
        def ways_no_a(n):
            if n < 3:
                return [1, 2, 4][n]
            # Can append P, PL, PLL to valid record
            return (ways_no_a(n-1) + ways_no_a(n-2) + ways_no_a(n-3)) % MOD
        
        return (ways_no_a(n) + sum(
            # Each place we can place the A splits into 2 parts without A
            ways_no_a(i) * ways_no_a(n-i-1) % MOD
            for i in range(n)
        )) % MOD