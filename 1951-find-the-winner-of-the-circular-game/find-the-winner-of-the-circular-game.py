class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(list(range(1, n+1)))
        i = 0
        while queue:
            player = queue.popleft()
            i += 1
            if i % k != 0:
                queue.append(player)
            elif not queue:
                return player