class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1 for i in range(n)]
        sufixes = [1 for _ in range(n)]
        prefixes[0] = nums[0]
        sufixes[n-1] = nums[n-1]

        for i in range(1, n):
            prefixes[i] *= prefixes[i-1] * nums[i]
            sufixes[n-1-i] *= sufixes[n-i] * nums[n-1-i]
        
        for i in range(n):
            nums[i] = 1
            if i > 0:
                nums[i] *= prefixes[i-1]
            if i < n - 1:
                nums[i] *= sufixes[i+1]
        return nums

        