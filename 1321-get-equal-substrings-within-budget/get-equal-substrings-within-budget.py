class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(t[i]) - ord(s[i])) for i in range(len(s))]
        n = len(s)

        max_len = 0
        j = 0
        current_cost = 0

        for i in range(n):
            if i > j:
                j = i
                current_cost = 0
            while j < len(s) and current_cost + cost[j] <= maxCost:
                current_cost += cost[j]
                j += 1
            max_len = max(max_len, j - i)
            current_cost -= cost[i]
            i += 1

        return max_len
            
        