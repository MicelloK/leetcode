class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        dist = 0
        for el in count:
            if count[el] == 1:
                dist += 1
            if dist == k:
                return el
        return ''