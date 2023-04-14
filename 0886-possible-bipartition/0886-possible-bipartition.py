class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1,n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)

        colors = [-1] * (n+1)  # initialize colors array
        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == -1 and not dfs(neighbor, 1-color):
                    return False
            return True

        for i in range(1,n+1):
            if colors[i] == -1 and not dfs(i, 0):
                return False
        return True  # return True if a valid division is found

        
        
        
        #         graph = defaultdict(list)
#         for n1,n2 in dislikes:
#             graph[n1].append(n2)
#             graph[n2].append(n1)

        
#         totalVisit = set()
        
#         map = [set(),set()]
#         def result(node,group):
#             for friend in graph[node]:
#                 if friend in map[group]:
#                     return False
#                 map[1-group].add(friend)
#                 if friend not in totalVisit:
#                     totalVisit.add(friend)
#                     result(friend,1-group)
#             return True


#         for i in range(1,n+1):
#             if i not in totalVisit:
#                 totalVisit.add(i)
#                 mm = result(i,0)
#                 if len(totalVisit)==n:
#                     if not mm:
#                         return False
                    
#         return True

