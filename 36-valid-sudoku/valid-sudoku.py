class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element != '.' and (element in rows[i] or element in cols[j] or element in sqrs[(i//3)*3+j//3]):
                    return False
                rows[i].add(element)
                cols[j].add(element)
                sqrs[(i//3)*3+j//3].add(element)
        return True
                

        