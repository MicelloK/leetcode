class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        freq = {}
        for key, val in count.items():
            if val in freq:
                freq[val].append(key)
            else:
                freq[val] = [key]
        result = []
        for f in sorted(freq.keys()):
            for val in sorted(freq[f], reverse=True):
                result += [val] * f
        return result

            
        