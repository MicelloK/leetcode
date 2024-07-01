class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons = 0
        for num in arr:
            if num % 2 == 0:
                cons = 0
            else:
                cons += 1
            if cons == 3:
                return True
        return False