class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (time // (n - 1)) % 2 == 0:
            return 1 + time % (n - 1)
        return n - time % (n - 1)