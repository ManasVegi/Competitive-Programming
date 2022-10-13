List = list
from collections import deque
class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for edge in prerequisites:
            u, v = edge
            if u in adjList:
                adjList[u].append(v)
            else:
                adjList[u] = [v]
        visited = set()
        def dfs(u, soFar):
            if u in visited or u not in adjList: #already saw this and it was ok or leaf node
                return True
            if u in soFar: #cycle
                return False
            soFar.add(u)
            for v in adjList[u]:
                if not dfs(v, soFar):
                    return False
            soFar.remove(u)
            visited.add(u)
            return True
        for u in adjList:
            if u not in visited and not dfs(u, set()):
                return False
        return True
    #much better memory due to no stack
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        indeg = {}
        for edge in prerequisites:
            u, v = edge
            if u in adjList:
                adjList[u].append(v)
            else:
                adjList[u] = [v]
            indeg[v] = indeg.get(v, 0) + 1
            indeg[u] = indeg.get(u, 0)
        q = deque()
        for u in indeg:
            if indeg[u] == 0:
                q.append(u)
        visited = set()
        while (len(q) > 0):
            n = len(q)
            for _ in range(n):
                u = q.popleft()
                if u in visited or u not in adjList:
                    continue
                visited.add(u)
                for v in adjList[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
        
          
        return len(visited) == len(adjList)