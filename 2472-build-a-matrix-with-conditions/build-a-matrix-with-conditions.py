class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(adj, V):
            indegree = [0] * V
            for i in range(V):
                for vertex in adj[i]:
                    indegree[vertex] += 1

            q = deque()
            for i in range(V):
                if indegree[i] == 0:
                    q.append(i)
            result = []
            while q:
                node = q.popleft()
                result.append(node)
                for adjacent in adj[node]:
                    indegree[adjacent] -= 1
                    if indegree[adjacent] == 0:
                        q.append(adjacent)

            if len(result) != V:
                return []
            return result

        
        for i in range(len(rowConditions)):
            rowConditions[i][0] -= 1
            rowConditions[i][1] -= 1
        
        adj = [[] for _ in range(k)]
        for edge in rowConditions:
            adj[edge[0]].append(edge[1])
        rows = topological_sort(adj, k)
        if not rows:
            return []

        for i in range(len(colConditions)):
            colConditions[i][0] -= 1
            colConditions[i][1] -= 1
        
        adj = [[] for _ in range(k)]
        for edge in colConditions:
            adj[edge[0]].append(edge[1])
        cols = topological_sort(adj, k)
        if not cols:
            return []

        result = [[0] * k for _ in range(k)]
        for i, el in enumerate(rows):
            j = cols.index(el)
            result[i][j] = el+1

        return result

        
        