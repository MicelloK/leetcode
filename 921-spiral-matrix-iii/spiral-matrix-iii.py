class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        move_len = 1
        current_dir_idx = 0
        result = [[rStart, cStart]]

        while len(result) < rows * cols:
            x_dir, y_dir = DIRECTIONS[current_dir_idx]
            for _ in range(move_len):
                rStart += y_dir
                cStart += x_dir
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    result.append([rStart, cStart])
            current_dir_idx = (current_dir_idx + 1) % len(DIRECTIONS)
            if current_dir_idx % 2 == 0:
                move_len += 1
        return result

