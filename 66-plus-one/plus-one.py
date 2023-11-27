class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits)
        if digits[index - 1] != 9:
            digits[index - 1] += 1
            return digits
        else:
            while True:
                if digits[index - 1] != 9 or (index == 1 and digits[index - 1] == 9):
                    break
                digits[index - 1] = (digits[index - 1] + 1) % 10
                index -= 1
            if index == 1 and digits[index - 1] == 9:
                digits[index - 1] = (digits[index - 1] + 1) % 10
                digits.append(0)
            digits[index - 1] += 1
        return digits
