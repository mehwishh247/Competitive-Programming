class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        def bfs(start,needed):
            visited = set()
            queue = deque()
            queue.append(start)
            while queue:
                node = queue.popleft()
                if node==needed:
                    return True
                if node not in visited:
                    visited.add(node)
                    for i in neighbors[node]:
                        if i not in visited:
                            queue.append(i)
            return False
        

        return bfs(source,destination)

        