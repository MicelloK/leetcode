class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_pointer = 0
        ones_pointer = 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[zeros_pointer], nums[i] = nums[i], nums[zeros_pointer]
                if nums[i] < nums[ones_pointer]:
                    nums[i], nums[ones_pointer] = nums[ones_pointer], nums[i]
                zeros_pointer += 1
                ones_pointer += 1
            elif num == 1:
                nums[ones_pointer], nums[i] = nums[i], nums[ones_pointer]
                ones_pointer += 1

        