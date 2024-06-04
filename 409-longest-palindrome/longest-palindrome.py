class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        odd = 0
        for v in count.values():
            result += v//2 * 2
            if v % 2 == 1:
                odd = 1
        return result + odd