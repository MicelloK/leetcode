class Solution:
    def numSteps(self, s: str) -> int:
        nums = [int(num) for num in s][::-1]
        
        result = 0
        rest = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                if num + rest == 2:
                    result += 1
            elif num + rest == 1:
                result += 2
                rest = 1
            elif num + rest == 2:
                result += 1
                rest = 1
            else:
                result += 1
                rest = 0
        
        return result



            
