class Solution:
    def checkRecord(self, n: int) -> int:
        visited = [[[None for _ in range(3)] for _ in range(2)] for _ in range(n)]

        def visit(n, a, l) -> int:
            '''
            returns num of eligible records where
            n = len
            a = num of 'A' - [0, 1]
            l = max num of 'L' at the begining - [0, 1, 2]
            '''
            if n == 1:
                if a == 1:
                    return 1
                if l > 0:
                    return 2
                return 1

            result = 0
            # L
            if l > 0:
                if visited[n-1][a][l-1] == None:
                    visited[n-1][a][l-1] = visit(n-1, a, l-1)
                result += visited[n-1][a][l-1]
            # A
            if a == 1:
                if visited[n-1][0][2] == None:
                    visited[n-1][0][2] = visit(n-1, 0, 2)
                result += visited[n-1][0][2]
            # P
            if visited[n-1][a][2] == None:
                visited[n-1][a][2] = visit(n-1, a, 2)
            result += visited[n-1][a][2]

            return result % (10 ** 9 + 7)

        return (visit(n, 0, 2) + visit(n, 1, 2)) % (10 ** 9 + 7)
                


            

            
            
        