class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [heights.count(i+1) for i in range(100)]
        i = 0
        j = 0
        result = 0
        while i < len(heights) and j < 100:
            while count[j] > 0:
                if heights[i] != j+1:
                    result += 1
                count[j] -= 1
                i += 1
            j += 1
        return result

