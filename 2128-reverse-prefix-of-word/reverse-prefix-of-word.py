class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        string = ""
        time = 1
        for char in word:
            string += char
            if time == 1 and char == ch:
                string = string[::-1]
                time = 0
        return string