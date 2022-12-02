List = list
from collections import deque
from collections import defaultdict
class Solution:
    #code could be more concise
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        topo = []
        while (len(q) > 0):
            n = len(q)
            for _ in range(n):
                u = q.popleft()
                if u in visited:
                    continue
                topo.append(u)
                if u not in adjList:
                    continue
                visited.add(u)
                for v in adjList[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
        
        #add all courses without any prereq
        for c in range(numCourses):
            if c not in indeg:
                topo.append(c) 
        #need to reverse topo due to the direction of my edges, from course -> prereq 
        return reversed(topo) if len(visited) == len(adjList) else []\

    def findOrderDfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        visited = set()
        ans = []
        def dfs(u, soFar):
            if u in soFar:
                return False
            if u in visited:
                return True
            visited.add(u)
            if u not in adjList:
                ans.append(u)
                return True
            soFar.add(u)
            for v in adjList[u]:
                if not dfs(v, soFar):
                    return False
            ans.append(u)
            soFar.remove(u)
            return True
        for u in adjList:
            if u not in visited:
                if not dfs(u, set()):
                    return []
        for u in range(numCourses):
            if u not in visited:
                ans.append(u)
        return ans
    
        
