class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                result += customers[i]
                customers[i] = 0
        
        grumpy_sum = 0
        for i in range(minutes):
            grumpy_sum += customers[i]
        
        max_grumpy = grumpy_sum
        for i in range(minutes, len(customers)):
            grumpy_sum -= customers[i-minutes]
            grumpy_sum += customers[i]
            max_grumpy = max(max_grumpy, grumpy_sum)
        return result + max_grumpy