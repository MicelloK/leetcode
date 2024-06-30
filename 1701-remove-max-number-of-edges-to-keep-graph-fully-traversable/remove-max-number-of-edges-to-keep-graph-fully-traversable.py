class Dsu:
    def __init__(self, n: int):
        self.elements = [x for x in range(1, n+1)]
        self.parents = deepcopy(self.elements)
        self.rank = [1 for _ in range(n)]

    def in_component(self, u: int, v: int):
        return self.find(u) == self.find(v)

    def completed(self):
        found_parents = set()
        for e in self.elements:
            found_parents.add(self.find(e))
        return len(found_parents) == 1

    def find(self, v: int):
        if v == self.parents[v-1]:
                return v
        else:
            self.parents[v-1] = self.find(self.parents[v-1])
            return self.parents[v-1]

    def union(self, u: int, v: int):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        
        if self.rank[u-1] > self.rank[v-1]:
            self.parents[v-1] = u
            self.rank[u-1] += self.rank[v-1]
        else:
            self.parents[u-1] = v
            self.rank[v-1] += self.rank[u-1]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a_dsu = Dsu(n)
        b_dsu = Dsu(n)

        result = 0
        for edge_type, u, v in edges:
            if edge_type == 3:
                if not a_dsu.in_component(u, v):
                    result += 1
                    a_dsu.union(u, v)
                    b_dsu.union(u, v)
        
        for edge_type, u, v in edges:
            if edge_type == 1:
                if not a_dsu.in_component(u, v):
                    result += 1
                    a_dsu.union(u, v)
            elif edge_type == 2:
                if not b_dsu.in_component(u, v):
                    result += 1
                    b_dsu.union(u, v)
        
        if not a_dsu.completed() or not b_dsu.completed():
            return -1
        return len(edges) - result
