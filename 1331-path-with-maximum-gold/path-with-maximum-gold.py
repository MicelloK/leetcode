class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def _in_boundary(i: int, j: int) -> bool:
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
        
        def _rec(i: int, j: int) -> int:
            visited[i][j] = True
            results = []
            if _in_boundary(i+1, j) and visited[i+1][j] == False and grid[i+1][j] != 0:
                results.append(_rec(i+1, j))
            if _in_boundary(i-1, j) and visited[i-1][j] == False and grid[i-1][j] != 0:
                results.append(_rec(i-1, j))
            if _in_boundary(i, j-1) and visited[i][j-1] == False and grid[i][j-1] != 0:
                results.append(_rec(i, j-1))
            if _in_boundary(i, j+1) and visited[i][j+1] == False and grid[i][j+1] != 0:
                results.append(_rec(i, j+1))
            visited[i][j] = False
            if results:
                return grid[i][j] + max(results)
            else:
                return grid[i][j]

        results = []
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element > 0:
                    results.append(_rec(i, j))
        if results:
            return max(results)
        return 0
            
            


