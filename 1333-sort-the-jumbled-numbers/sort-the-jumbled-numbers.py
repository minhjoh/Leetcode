class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            num = str(nums[i])
            tran_num = ""
            for char in num:
                map_char = mapping[int(char)]
                tran_num += str(map_char)
                
            li.append([int(tran_num), i])
        
        li.sort()
        res = []
        for num, index in li:
            res.append(nums[index])
        return res