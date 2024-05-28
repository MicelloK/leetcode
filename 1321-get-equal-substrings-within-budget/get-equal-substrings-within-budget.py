class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(t[i]) - ord(s[i])) for i in range(len(s))]
        n = len(s)

        max_len = 0
        l = 0
        current_cost = 0

        for r in range(n):
            current_cost += cost[r]

            while current_cost > maxCost:
                current_cost -= cost[l]
                l += 1
            
            max_len = max(max_len, r - l + 1)

        return max_len
            
        