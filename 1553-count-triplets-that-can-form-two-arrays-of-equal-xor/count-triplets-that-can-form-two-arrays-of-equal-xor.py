class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixes = [arr[0]]
        for i in range(1, len(arr)):
            prefixes.append(arr[i] ^ prefixes[len(prefixes)-1])
        
        result = 0
        for i in range(len(arr)-1):
            for k in range(i+1, len(arr)):
                if i == 0 and prefixes[k] == 0 or i > 0 and prefixes[k] ^ prefixes[i-1] == 0:
                    result += k - i
        return result
                

        