class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(e1 != e2 for e1, e2 in zip(heights, expected))