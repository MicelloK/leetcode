class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        profit = 0
        max_profit = 0
        i = 0
        j = 0
        while j < len(worker):
            while i < len(jobs) and jobs[i][0] <= worker[j]:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            profit += max_profit
            j += 1
        return profit


        