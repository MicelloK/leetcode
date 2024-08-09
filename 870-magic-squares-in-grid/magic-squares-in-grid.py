class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def check_grid(grid):
            sums = set()
            for row in grid:
                sums.add(sum(row))

            for i in range(len(grid)):
                col_sum = 0
                for j in range(len(grid)):
                    col_sum += grid[j][i]
                sums.add(col_sum)
            
            sums.add(grid[0][0] + grid[1][1] + grid[2][2])
            sums.add(grid[0][2] + grid[1][1] + grid[2][0])

            elements = [e for row in grid for e in row]
            for i in range(1, 10):
                if i not in elements:
                    return False
            
            distinct_numbers = True


            return len(sums) == 1

        result = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [grid[k][j:j+3] for k in range(i, i+3)]
                if check_grid(subgrid):
                    result += 1

        return result