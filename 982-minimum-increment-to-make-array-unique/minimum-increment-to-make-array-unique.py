class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        result = 0
        last = -1
        for num, val in count.items():
            result += (val-1) * val // 2

            if num > last:
                last = num + val - 1
            else:
                result += (last - num + 1) * val
                last = last + val
        return result
            
