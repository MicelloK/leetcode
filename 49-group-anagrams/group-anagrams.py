from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            grouped.setdefault(sorted_str, []).append(string)
        return list(grouped.values())
