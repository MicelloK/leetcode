class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-1):
            if nums[i] >= i+1 and nums[i+1] < i+1:
                return i+1
        if nums[len(nums)-1] >= len(nums):
            return len(nums)
        return -1