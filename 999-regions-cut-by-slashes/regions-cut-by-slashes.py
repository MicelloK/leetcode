class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        graph = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == ' ':
                    graph[(i, j, 0)].extend([(i, j, 1), (i, j, 3)])
                    graph[(i, j, 1)].extend([(i, j, 2), (i, j, 0)])
                    graph[(i, j, 2)].extend([(i, j, 1), (i, j, 3)])
                    graph[(i, j, 3)].extend([(i, j, 0), (i, j, 2)])
                elif grid[i][j] == '/':
                    graph[(i, j, 0)].append((i, j, 3))
                    graph[(i, j, 1)].append((i, j, 2))
                    graph[(i, j, 2)].append((i, j, 1))
                    graph[(i, j, 3)].append((i, j, 0))
                elif grid[i][j] == '\\':
                    graph[(i, j, 0)].append((i, j, 1))
                    graph[(i, j, 1)].append((i, j, 0))
                    graph[(i, j, 2)].append((i, j, 3))
                    graph[(i, j, 3)].append((i, j, 2))

                if i > 0:
                    graph[(i, j, 0)].append((i-1, j, 2))
                if j < n-1:
                    graph[(i, j, 1)].append((i, j+1, 3))
                if i < n-1:
                    graph[(i, j, 2)].append((i+1, j, 0))
                if j > 0:
                    graph[(i, j, 3)].append((i, j-1, 1))

        visited = {}
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    visited[(i, j, k)] = False

        def bfs(start):
            queue = deque([start])
            visited[start] = True

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        result = 0
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not visited[(i, j , k)]:
                        result += 1
                        bfs((i, j, k))
        return result
