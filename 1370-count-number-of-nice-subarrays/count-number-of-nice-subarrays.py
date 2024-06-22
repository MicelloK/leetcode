class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd = [0]
        last_prefix = 0
        for num in nums:
            if num % 2 == 1:
                last_prefix += 1
            prefix_odd.append(last_prefix)
        
        count = {}
        for odds in prefix_odd:
            if odds in count:
                count[odds] += 1
            else:
                count[odds] = 1
        result = 0
        for el, val in count.items():
            if el + k in count:
                result += val * count[el+k]
        return result
