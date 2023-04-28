class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        
        visited = set([0])
        
        while queue:
            
            node= queue.popleft()
            visited.add(node)

            for kid in rooms[node]:
                if kid not in visited:
                    queue.append(kid)
        
        
        return len(visited)==len(rooms)
        