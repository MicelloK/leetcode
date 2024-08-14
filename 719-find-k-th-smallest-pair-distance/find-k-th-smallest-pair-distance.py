class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def lower_dist_num(x):
            result = 0
            i = 0
            for j in range(len(nums)):
                while nums[j] - nums[i] > x:
                    i += 1
                result += j - i
            return result

        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            if lower_dist_num(m) < k:
                l = m + 1
            else:
                r = m

        return l
