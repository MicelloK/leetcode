class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        occurrenced = {}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sum %= k
            if prefix_sum in occurrenced:
                result += occurrenced[prefix_sum]
                occurrenced[prefix_sum] += 1
            else:
                occurrenced[prefix_sum] = 1
            if prefix_sum == 0:
                result += 1
        return result

