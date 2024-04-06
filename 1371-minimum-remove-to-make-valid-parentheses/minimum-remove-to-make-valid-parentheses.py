class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        left_count = right_count = 0
        for ch in s:
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(ch)
            
        result = ""
        while stack:
            curr_char = stack.pop()
            if left_count > right_count and curr_char == '(':
                left_count -= 1
            else:
                result += curr_char
                
        return result[::-1]
            