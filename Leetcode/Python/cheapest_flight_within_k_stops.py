from collections import defaultdict
#using bellman ford algo
List = list
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMat = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for flight in flights:
            f, t, p = flight
            adjMat[f][t] = p
        distances = defaultdict(lambda: float('inf'))
        distances[(src, 0)] = 0
        bestResult = float('inf')
        for i in range(1, k + 2):
            for u in adjMat:
                for v in adjMat[u]:
                    if v == u or distances[(u, i - 1)] == float('inf'):
                        continue
                    distances[(v, i)] = min(distances[(v, i)], distances[(u, i - 1)] + adjMat[u][v])
                    if v == dst:
                        bestResult = min(bestResult, distances[(dst, i)])
        return -1 if bestResult == float('inf') else bestResult

    def findCheapestPriceClean(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = defaultdict(lambda: float('inf'))
        dists[(src, -1)] = 0
        for d in range(k + 1):
            for u, v, w in flights:
                if (u, d - 1) in dists:
                    dists[(v, d)] = min(dists[(v, d)], w + dists[(u, d - 1)])
                    dists[(u, d)] = min(dists[(u, d)], dists[(u, d - 1)])
        return dists[(dst, k)] if (dst, k) in dists else -1

    def findCheapestPriceCleanBetterMemory(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prevdists = defaultdict(lambda: float('inf'))
        prevdists[src] = 0
        for d in range(k + 1):
            currdists = defaultdict(lambda: float('inf'))
            for u, v, w in flights:
                if u in prevdists:
                    currdists[v] = min(currdists[v], w + prevdists[u])
                    currdists[u] = min(currdists[u], prevdists[u])
            prevdists = currdists
        return prevdists[dst] if dst in prevdists else -1

    def findCheapestPriceBetterMemory(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMat = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for flight in flights:
            f, t, p = flight
            adjMat[f][t] = p
        prev, curr = defaultdict(lambda: float('inf')), defaultdict(lambda: float('inf'))
        prev[src] = 0
        bestResult = float('inf')
        for i in range(1, k + 2):
            for u in adjMat:
                for v in adjMat[u]:
                    if v == u or prev[u] == float('inf'):
                        continue
                    curr[v] = min(curr[v], prev[u] + adjMat[u][v])
                    if v == dst:
                        bestResult = min(bestResult, curr[v])
            prev = curr
            curr = defaultdict(lambda: float('inf'))
        return -1 if bestResult == float('inf') else bestResult