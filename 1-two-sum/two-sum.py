class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rests = {}
        for i, element in enumerate(nums):
            if element in rests and i != rests[element]:
                return [i, rests[element]]
            rest = target - element
            rests[rest] = i
            
            
