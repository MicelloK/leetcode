class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l <= r:
            pow_sum = l ** 2 + r ** 2
            if pow_sum == c:
                return True
            if pow_sum < c:
                l += 1
            else:
                r -= 1
        return False