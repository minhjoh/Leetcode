class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = [0 for i in range(len(words))]
        word_score = [0 for i in range(len(words))]
        letters_freq = [0 for i in range(26)]

        # Calculate the frequency of each letter in letters
        for letter in letters:
            letters_freq[ord(letter) - ord('a')] += 1

        # Calculate the score for each word
        for idx in range(len(words)):
            word = words[idx]
            for c in word:
                code = ord(c) - ord('a')
                if letters_freq[code] > 0:
                    word_score[idx] += score[code]
                else:
                    word_score[idx] = -1
                    break

        state = set()

        # Backtracking function to explore word combinations
        def backtrack(word_idx, score, permutation_key, l_freq):
            permutation_key |= (1 << word_idx)
            if word_idx == len(words):
                return
            if permutation_key in state:
                return
            if word_score[word_idx] == -1:
                return
            for i in range(26):
                if l_freq[i] > letters_freq[i]:
                    return
            state.add(permutation_key)
            score += word_score[word_idx]
            scores[word_idx] = max(scores[word_idx], score)
            for idx in range(word_idx + 1, len(words)):
                for c in words[idx]:
                    code = ord(c) - ord('a')
                    l_freq[code] += 1
                backtrack(idx, score, permutation_key, l_freq)
                for c in words[idx]:
                    code = ord(c) - ord('a')
                    l_freq[code] -= 1

        result = 0
        for idx in range(len(words)):
            l_freq = [0 for i in range(26)]
            for c in words[idx]:
                code = ord(c) - ord('a')
                l_freq[code] += 1
            permutation_key = 1 << idx
            backtrack(idx, 0, permutation_key, l_freq)
            result = max(result, scores[idx])

        return result