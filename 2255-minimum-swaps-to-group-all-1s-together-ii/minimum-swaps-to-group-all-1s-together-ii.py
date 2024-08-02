class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        current_count = nums[:ones_count].count(1)
        result = float('inf')
        for i in range(len(nums)):
            result = min(result, ones_count-current_count)

            if nums[i] == 1:
                current_count -= 1
            if nums[(i + ones_count) % len(nums)] == 1:
                current_count += 1

        return result