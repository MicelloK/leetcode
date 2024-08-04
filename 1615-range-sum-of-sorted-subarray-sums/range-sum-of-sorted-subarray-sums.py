class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        nums_sum = sum(nums)
        prefixes = []
        current_sum = 0
        for num in nums:
            current_sum += num
            prefixes.append(current_sum)

        result = []
        for i in range(len(nums)):
            result.append(prefixes[i])
            for j in range(i):
                result.append(prefixes[i] - prefixes[j])
                
        return sum(sorted(result)[left-1:right]) % (10 ** 9 + 7)