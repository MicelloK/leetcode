class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {x: arr1.count(x) for x in arr2}
        result = []
        for x, val in count.items():
            result += [x] * val
        
        arr1.sort()
        for x in arr1:
            if x not in count:
                result.append(x)
        return result