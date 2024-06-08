class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix = 0
        occurrence = {}
        for i, num in enumerate(nums):
            prefix += num
            print(prefix, prefix%k)
            prefix %= k
            if i > 0 and prefix == 0:
                return True
            elif prefix in occurrence and i - occurrence[prefix] >= 2:
                return True
            elif prefix not in occurrence:
                occurrence[prefix] = i
        return False

