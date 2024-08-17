class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for r in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for i in range(1, n):
                left[i] = max(left[i - 1] - 1, dp[i])

            right[n - 1] = dp[n - 1]
            for i in range(n - 2, -1, -1):
                right[i] = max(right[i + 1] - 1, dp[i])

            for i in range(n):
                dp[i] = points[r][i] + max(left[i], right[i])

        return max(dp)

