class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        result = []
        for num, c in count.items():
            if c == 1:
                result.append(num)
        return result
        