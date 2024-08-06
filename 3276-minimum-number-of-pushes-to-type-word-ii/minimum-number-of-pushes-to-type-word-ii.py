class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        mapped_letters = 0
        for letter, count in sorted(Counter(word).items(), key=lambda x: x[1], reverse=True):
            result += count * (mapped_letters // 8 + 1)
            mapped_letters += 1
        return result