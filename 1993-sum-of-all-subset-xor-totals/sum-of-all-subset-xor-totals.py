class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a|=i
        return a* (1<<(len(nums)-1))

        # total_xor = 0
        # for i in range(2**len(nums)):
        #     partial_xor = 0
        #     for j in range(len(nums)):
        #         if i & (1 << j):
        #             partial_xor ^= nums[j]
        #     total_xor += partial_xor
        # return total_xor
