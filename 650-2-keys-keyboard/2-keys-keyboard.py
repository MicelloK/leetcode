class Solution:
    @lru_cache
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        result = n
        for i in range(n-1, 1, -1):
            if n % i == 0:
                result = min(result, n//i + self.minSteps(i))
        return result

