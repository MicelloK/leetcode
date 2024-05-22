class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        for val in nums:
            if val != min_val and val != max_val:
                return val
        return -1