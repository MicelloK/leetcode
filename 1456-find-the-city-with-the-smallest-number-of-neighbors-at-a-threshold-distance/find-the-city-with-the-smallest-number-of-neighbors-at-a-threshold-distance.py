class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def floyd_warschall(n: int, graph: List[List[int]]) -> List[List[int]]:
            dist = [[float('inf') for _ in range(n)] for _ in range(n)]
            for edge in graph:
                f, t, w = edge
                dist[f][t] = w
                dist[t][f] = w

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist
        
        dist = floyd_warschall(n, edges)
        min_city = -1
        min_num = float('inf')
        for i, row in enumerate(dist):
            city_num = sum([1 if num <= distanceThreshold and i != j else 0 for j, num in enumerate(row)])
            if city_num <= min_num:
                min_city = i
                min_num = city_num
        return min_city



