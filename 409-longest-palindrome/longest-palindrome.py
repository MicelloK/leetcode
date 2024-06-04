class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        result = 0
        for _, v in count.items():
            result += v//2 * 2
        return min(result+1, len(s))