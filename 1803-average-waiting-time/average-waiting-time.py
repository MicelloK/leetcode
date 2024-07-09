class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last_time = 0
        result = 0
        for arrival, time in customers:
            last_time = max(last_time, arrival)
            last_time += time
            result += last_time - arrival
        return result / len(customers)