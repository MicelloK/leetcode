class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:        
        result = 0
        max_reachable = 0
        i = 0

        while max_reachable < n:
            if i < len(nums) and nums[i] <= max_reachable + 1:
                max_reachable += nums[i]
                i += 1
            else:
                max_reachable += max_reachable + 1
                result += 1

        return result


        