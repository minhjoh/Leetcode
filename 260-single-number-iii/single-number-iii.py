class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for num in nums:
            x^=num
        mask=x&-x
        ans1,ans2=0,0
        for num in nums:
            if num & mask:
                ans1^=num
            else:
                ans2^=num
        return [ans1,ans2]                