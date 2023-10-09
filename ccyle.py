
class Node:
    def __init__(self, src, dest, wgt):
        self.src = src
        self.dest = dest
        self.wgt = wgt

def bellman_ford():
    nodeInCycle = -1
    for i in range(1, n + 1):
        nodeInCycle = -1
        for e in edges:
            src = e.src
            dest = e.dest
            wgt = e.wgt
            if dist[src] + wgt < dist[dest]:
                dist[dest] = wgt + dist[src]
                relaxant[dest] = src
                nodeInCycle = dest
    
    if nodeInCycle == -1:
        print("NO")
    
    else:
        for i in range(1, n + 1):
            nodeInCycle = relaxant[nodeInCycle]
        
        cycle = []
        
        currNode = nodeInCycle
        while True:
            cycle.append(currNode)
            currNode = relaxant[currNode]
            if currNode == nodeInCycle and len(cycle) > 1:
                break
        
        cycle.reverse()
        
        print("YES")
        for node in cycle:
            print(node, end=" ")
        
        print()

n, m = map(int, input().split())
edges = []
dist = [float('inf')] * (n + 1)
relaxant = [-1] * (n + 1)

for i in range(m):
    src, dest, wgt = map(int, input().split())
    edges.append(Node(src, dest, wgt))

bellman_ford()
