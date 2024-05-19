class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        def xor(a: int, b: int) -> int:
            result = 0
            exp = 0
            while a > 0 or b > 0:
                if a % 2 != b % 2:
                    result += 2 ** exp
                exp += 1
                a //= 2
                b //= 2
            return result

        xor_profit = [(x, xor(x, k) - x) for x in nums]
        xor_profit.sort(key=lambda x: x[1], reverse=True)

        result = 0
        while len(xor_profit) >= 2:
            v1 = xor_profit.pop(0)
            v2 = xor_profit.pop(0)
            if v1[1] + v2[1] > 0:
                result += v1[0] + v1[1] + v2[0] + v2[1]
            else:
                result += v1[0] + v2[0]
        while xor_profit:
            result += xor_profit.pop(0)[0]
        
        return result



        # graph = {}
        # for edge in edges:
        #     u, v = edge
        #     if u in graph:
        #         graph[u].append(v)
        #     else:
        #         graph[u] = [v]
        #     if v in graph:
        #         graph[v].append(u)
        #     else:
        #         graph[v] = [u]

        # changed_nums = [xor(x, k) for x in nums]
        
        # def visit(vertex: int, changed: bool) -> int:
        #     num_of_changes = 0
        #     if changed:
        #         num_of_changes += 1

        #     if not graph[vertex]:
        #         if changed:
        #             return changed_nums[vertex]
        #         else:
        #             return nums[vertex]

        #     neigh_vals = []
        #     for neigh in graph[vertex]:
        #         if vertex in graph[neigh]:
        #             graph[neigh].remove(vertex)
        #         neigh_vals.append((visit(neigh, False), visit(neigh, True)))
            
        #     childs_result = 0
        #     minimal_loss = abs(neigh_vals[0][0] - neigh_vals[0][1])
        #     for val in neigh_vals:
        #         if abs(val[0] - val[1]) < minimal_loss:
        #             minimal_loss = abs(val[0] - val[1])
        #         if val[0] > val[1]:
        #             childs_result += val[0]
        #         else:
        #             childs_result += val[1]
        #             num_of_changes += 1

        #     if nums[vertex] >= changed_nums[vertex] and num_of_changes % 2 == 0:
        #         return nums[vertex] + childs_result
        #     if changed_nums[vertex] >= nums[vertex] and num_of_changes % 2 == 1:
        #         return changed_nums[vertex] + childs_result
            
        #     if num_of_changes % 2 == 0:
        #         return max(nums[vertex] + childs_result, changed_nums[vertex] + childs_result - minimal_loss)
        #     else:
        #         return max(changed_nums[vertex] + childs_result, nums[vertex] + childs_result - minimal_loss)
        
        # return visit(0, False)

