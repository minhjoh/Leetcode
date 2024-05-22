class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        L = len(s)
        def backtracking(i, substring, choices):
            # finish condition
            if i >= L and not substring:
                self.answer.append(choices[:])
                return

            # decide to add current char to substring
            if i < L:
                backtracking(i+1, substring + s[i], choices)

            # if substring is palindrome, decide to add this substring to choice
            if substring and substring == substring[::-1]:
                choices.append(substring)
                backtracking(i+1, s[i] if i < L else "", choices)
                choices.pop()

        backtracking(0, "", [])
        return self.answer


            