class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles % (numExchange - 1) == 0:
            return numBottles + numBottles // (numExchange - 1) - 1
        return numBottles + numBottles // (numExchange - 1)
