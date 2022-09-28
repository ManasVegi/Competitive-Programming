from collections import defaultdict
List = list
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(lambda: defaultdict(lambda: -1))
        # -2 means visited but not possible
        
        def dfs(A, B):
            if adjList[A][B] != -1:
                return adjList[A][B]
            
            if A == B:
                return 1
            adjList[A][B] = -2
            for nei in adjList[A]:
                if nei == A:
                    continue
                if adjList[A][nei] > 0:
                    res = adjList[A][nei] * dfs(nei, B)
                    if res > 0:
                        adjList[A][B] = res
                        return res
            return -1
            
        for i, equation in enumerate(equations):
            A, B, v = equation[0], equation[1], values[i]
            if adjList[A][A] == -1:
                adjList[A][A] = 1
            if adjList[B][B] == -1:
                adjList[B][B] = 1
            if adjList[A][B] == -1: #already visited
                adjList[A][B] = v
                if v > 0:
                    adjList[B][A] = 1 / v
        ans = []
        for q in queries:
            C, D = q[0], q[1]
            if adjList[C][D] == -1:
                dfs(C, D)
            ans.append(-1 if adjList[C][D] == -2 else adjList[C][D])
        return ans

sol = Solution()
equations, values, queries = [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(sol.calcEquation(equations, values, queries))