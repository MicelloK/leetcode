class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = list(filter(lambda x: x % 2 == 0, nums))
        odds = list(filter(lambda x: x % 2 == 1, nums))
        return evens + odds
