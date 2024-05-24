class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words_scores = {}
        for word in words:
            word_score = 0
            for char in word:
                word_score += score[ord(char)-97]
            words_scores[word] = word_score

        words_counter = {word: Counter(word) for word in words}

        def visit(i: int, available) -> int:
            if i >= len(words):
                return 0

            max_val = visit(i+1, available)

            word = words[i]
            valid_word = True
            for char, count in words_counter[word].items():
                if available[char] < count:
                    valid_word = False

            if valid_word:
                new_available = available - words_counter[word]
                max_val = max(max_val, words_scores[word] + visit(i+1, new_available))

            return max_val

        available = Counter(letters)
        return visit(0, available)
