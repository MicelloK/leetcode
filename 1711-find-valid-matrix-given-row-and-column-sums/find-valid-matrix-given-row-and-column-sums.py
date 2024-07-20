class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0] * len(colSum) for _ in rowSum]
        i, j = 0, 0
        while i < len(rowSum) and j < len(colSum):
            value = min([rowSum[i], colSum[j]])
            result[i][j] = value
            rowSum[i] -= value
            colSum[j] -= value
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return result



