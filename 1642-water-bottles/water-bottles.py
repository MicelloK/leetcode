class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            result += numBottles // numExchange
            numBottles -= (numBottles // numExchange) * (numExchange - 1)
        return result

        # if numBottles % (numExchange - 1) == 0:
        #     return numBottles + numBottles // (numExchange - 1) - 1
        # return numBottles + numBottles // (numExchange - 1)
