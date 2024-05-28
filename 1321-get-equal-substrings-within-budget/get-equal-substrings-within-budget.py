class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        i = 0
        j = 0
        current_cost = 0
        while j < len(s):
            while j < len(s) and current_cost + abs(ord(t[j]) - ord(s[j])) <= maxCost:
                current_cost += abs(ord(t[j]) - ord(s[j]))
                j += 1
            max_len = max(max_len, j - i)
            current_cost -= abs(ord(t[i]) - ord(s[i]))
            i += 1
            if i > j:
                j = i
                current_cost = 0

        return max_len
            
        