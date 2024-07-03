class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        min_val = float('inf')
        for i in range(3):
            min_val = min(min_val, abs(nums[len(nums)-4+i] - nums[i]))
        return min(min_val, abs(nums[len(nums)-1] - nums[3]))
  