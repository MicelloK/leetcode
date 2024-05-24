class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words_scores = {word: sum(score[ord(char)-97] for char in word) for word in words}

        def visit(i: int, available, memo) -> int:
            if i >= len(words):
                return 0

            state = (i, tuple(available.items()))
            if state in memo:
                return memo[state]

            max_val = visit(i+1, available, memo)

            word = words[i]
            word_counter = Counter(word)
            valid_word = True
            for char, count in word_counter.items():
                if available[char] < count:
                    valid_word = False

            if valid_word:
                new_available = available - word_counter
                max_val = max(max_val, words_scores[word] + visit(i+1, new_available, memo))

            memo[state] = max_val
            return max_val

        available = Counter(letters)
        memo = {}
        return visit(0, available, memo)
