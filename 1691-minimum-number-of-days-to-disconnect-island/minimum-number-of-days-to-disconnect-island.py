class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == 0:
                return False
            visited[i][j] = True
            for i_dir, j_dir in DIRECTIONS:
                dfs(i + i_dir, j + j_dir)
            return True

        ones_count = len([el for row in grid for el in row if el == 1])
        if ones_count < 2:
            return ones_count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited = [[False for _ in grid[0]] for _ in grid]
                    visited[i][j] = True
                    result = 0
                    for i_dir, j_dir in DIRECTIONS:
                        if dfs(i + i_dir, j + j_dir):
                            result += 1
                    if len([el for row in visited for el in row if el == True]) != len([el for row in grid for el in row if el == 1]):
                        return 0
                    if result > 1:
                        return 1
        return 2

                
            
            

        
