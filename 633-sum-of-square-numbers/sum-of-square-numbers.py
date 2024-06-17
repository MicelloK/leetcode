class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = c // 2
        x = sqrt(x)
        i = x // 1
        j = x // 1
        while True:
            print(i, j, i ** 2 + j ** 2, c)
            if i ** 2 + j ** 2 == c:
                return True
            while i >= 0 and i ** 2 + j ** 2 < c:
                j += 1
            while i >= 0 and i ** 2 + j ** 2 > c:
                i -= 1
            if i < 0 and i ** 2 + j ** 2 != c:
                return False