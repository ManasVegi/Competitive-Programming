# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node
        adjList = {}
        def createAdjList(root):
            if root.val in adjList:
                return
            if root.val not in adjList:
                adjList[root.val] = []
            for nei in root.neighbors:
                adjList[root.val].append(nei.val)
                createAdjList(nei)
        createAdjList(node)
        nodes = {}
        for val in adjList:
            nodes[val] = Node(val)
        for val in adjList:
            newnode = nodes[val]
            newneighs = []
            for neival in adjList[val]:
                newneighs.append(nodes[neival])
            newnode.neighbors = newneighs
        return nodes[1]