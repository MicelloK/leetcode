class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0] * len(colSum) for _ in rowSum]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                value = min([rowSum[i], colSum[j]])
                result[i][j] = value
                rowSum[i] -= value
                colSum[j] -= value
        return result



