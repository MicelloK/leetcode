class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = list(accumulate(reversed(piles)))[::-1]
        
        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0

            max_score = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                max_score = max(max_score, suffix_sum[i] - dp(i + x, max(m, x)))
            
            return max_score

        return dp(0, 1)
