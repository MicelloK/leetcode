class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        days = list(set(bloomDay))
        days.sort()
        minDay = 1000_000_000_0
        l = 0
        r = len(days) - 1
        while l <= r:
            mid = l + (r - l) // 2

            result = 0
            group = 0
            for x in bloomDay:
                if x > days[mid]:
                    result += group // k
                    group = 0
                else:
                    group += 1
            result += group // k

            if result >= m:
                minDay = min(minDay, days[mid])
                r = mid - 1
            else:
                l = mid + 1

        if minDay == 1000_000_000_0:
            return -1
        return minDay