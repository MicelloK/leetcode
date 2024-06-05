class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = {c: words[0].count(c) for c in words[0]}
        for i in range(1, len(words)):
            for c in result.keys():
                result[c] = min(result[c], words[i].count(c))
        result_list = []
        for c, v in result.items():
            if v > 0:
                result_list += [c] * v
        return result_list
        

