from queue import PriorityQueue
from collections import deque
from copy import deepcopy

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # find cell factors
        n = len(grid)
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cell_factors = [[-1 for _ in range(n)] for _ in range(n)]
        q = deque()
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element == 1:
                    cell_factors[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for direction in DIRECTIONS:
                new_i, new_j = i + direction[0], j + direction[1]
                if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n and cell_factors[new_i][new_j] == -1:
                    cell_factors[new_i][new_j] = cell_factors[i][j] + 1
                    q.append((new_i, new_j))

        # find the best path
        safeness_factor = n * n
        q = PriorityQueue()
        q.put((-cell_factors[0][0], (0, 0)))
        grid[0][0] = -1 # visited :)
        while q:
            priority, coords = q.get()
            if -priority < safeness_factor:
                safeness_factor = -priority
            i, j = coords
            if i == n - 1 and j == n - 1:
                return safeness_factor
            for direction in DIRECTIONS:
                new_i, new_j = i + direction[0], j + direction[1]
                if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n and grid[new_i][new_j] != -1:
                    grid[new_i][new_j] = -1
                    q.put((-cell_factors[new_i][new_j], (new_i, new_j)))









        
