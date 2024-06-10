class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = sum(e1 != e2 for e1, e2 in zip(heights, expected))
        return count