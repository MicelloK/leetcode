from queue import PriorityQueue

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w > max(capital):
            return w + sum(nlargest(k, profits))

        sorted_projects = sorted(zip(capital, profits))
        next_proj = 0
        projects = PriorityQueue()
        while next_proj < len(sorted_projects) and sorted_projects[next_proj][0] <= w:
            projects.put(-sorted_projects[next_proj][1])
            next_proj += 1
        
        while not projects.empty():
            prof = -projects.get()
            w += prof
            k -= 1
            if k == 0:
                return w
            while next_proj < len(sorted_projects) and sorted_projects[next_proj][0] <= w:
                projects.put(-sorted_projects[next_proj][1])
                next_proj += 1
        return w
