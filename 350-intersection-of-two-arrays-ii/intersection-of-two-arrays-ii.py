class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        intersection = count1 & count2
        result = []
        for el in intersection:
            result += [el] * intersection[el]
        return result