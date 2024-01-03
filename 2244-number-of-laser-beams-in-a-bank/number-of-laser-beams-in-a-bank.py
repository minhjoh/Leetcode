class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        if len(bank) < 2:
            return 0
        count = count_one = temp = 0
        for string in bank:
            temp = count_one
            for chr in string:
                if chr == '1':
                    count_one += 1
            if temp != count_one and temp != 0:
                count = count + temp * (count_one - temp)
                count_one = count_one - temp
        return count