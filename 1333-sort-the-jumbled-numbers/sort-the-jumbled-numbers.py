class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda num: int(''.join(str(mapping[int(ch)]) for ch in str(num))))