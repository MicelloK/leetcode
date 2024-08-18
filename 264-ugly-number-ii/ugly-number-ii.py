class Solution:
    def nthUglyNumber(self, n: int) -> int:
        queue = [1]
        heaped = set()
        for _ in range(n-1):
            smallest_ugly = heapq.heappop(queue)
            for x in [2, 3, 5]:
                if smallest_ugly * x not in heaped:
                    heaped.add(smallest_ugly * x)
                    heapq.heappush(queue, smallest_ugly * x)

        return heapq.heappop(queue)

