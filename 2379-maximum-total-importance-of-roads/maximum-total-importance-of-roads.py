class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = {}
        for road in roads:
            for city in road:
                if city in count:
                    count[city] += 1
                else:
                    count[city] = 1
        
        cities = list(count.values())
        cities.sort(reverse=True)
        result = 0
        for city in cities:
            result += city * n
            n -= 1
        return result