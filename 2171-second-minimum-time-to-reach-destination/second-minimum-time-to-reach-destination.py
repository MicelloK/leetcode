class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def bfs_all_paths(graph, start, end):
            queue = deque([(start, 0)])
            distances = [float('inf')] * n
            second_distances = [float('inf')] * n
            distances[start] = 0

            while queue:
                current, dist = queue.popleft()
                
                for neighbor in graph[current]:
                    if dist + 1 < distances[neighbor]:
                        distances[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))
                    elif distances[neighbor] < dist + 1 < second_distances[neighbor]:
                        second_distances[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))

            return second_distances[end]

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        second_shortest_length = bfs_all_paths(graph, 0, n-1)

        time_elapsed = 0
        for _ in range(second_shortest_length):
            if (time_elapsed // change) % 2 == 1:
                time_elapsed += change - (time_elapsed % change)
            time_elapsed += time

        return time_elapsed
