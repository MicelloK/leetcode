class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        memo = {}

        def rek(start, target):
            if target == 0:
                return [[]]
            if (start, target) in memo:
                return memo[(start, target)]
            
            combinations = []
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                for comb in rek(i + 1, target - candidates[i]):
                    combinations.append([candidates[i]] + comb)
            
            memo[(start, target)] = combinations
            return combinations

        result = rek(0, target)
        return result
