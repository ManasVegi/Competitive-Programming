List = list
from collections import deque
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
        return reversed(topo) if len(visited) == len(adjList) else []