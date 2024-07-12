class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, pair: str, value: int) -> (str, int):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == pair:
                    stack.pop()
                    score += value
                else:
                    stack.append(char)
            return ''.join(stack), score

        if len(s) <= 1:
            return 0

        total_score = 0
        if x > y:
            s, score = remove_pairs(s, 'ab', x)
            total_score += score
            s, score = remove_pairs(s, 'ba', y)
            total_score += score
        else:
            s, score = remove_pairs(s, 'ba', y)
            total_score += score
            s, score = remove_pairs(s, 'ab', x)
            total_score += score

        return total_score
