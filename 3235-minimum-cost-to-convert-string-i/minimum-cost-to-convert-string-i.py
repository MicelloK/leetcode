class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf') for _ in range(26)] for _ in range(26)]
        for o, ch, weight in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(ch) - ord('a')] = min(weight, dist[ord(o) - ord('a')][ord(ch) - ord('a')])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        result = 0
        for s, t in zip(source, target):
            d = dist[ord(s) - ord('a')][ord(t) - ord('a')]
            if s != t:
                if d == float('inf'):
                    return -1
                result += d
        return result