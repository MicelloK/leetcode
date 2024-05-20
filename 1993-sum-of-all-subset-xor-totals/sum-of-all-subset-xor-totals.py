class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor = 0
        for i in range(2**len(nums)):
            partial_xor = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    partial_xor ^= nums[j]
            total_xor += partial_xor
        return total_xor
