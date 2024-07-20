class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = [min(row) for row in matrix]
        for column_index in range(len(matrix[0])):
            column_values_with_indices = [(row[column_index], i) for i, row in enumerate(matrix)]
            max_value, max_index = max(column_values_with_indices, key=lambda x: x[0])
            if max_index < len(rows) and rows[max_index] == max_value:
                result.append(max_value)
        return result