class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = []
            for res in result:
                new_subsets.append(res + [num])
            result += new_subsets
        return result