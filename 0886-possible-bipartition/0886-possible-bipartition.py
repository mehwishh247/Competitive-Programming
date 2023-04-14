class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1,n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)

        
        totalVisit = set()
        
        map = [set(),set()]
        def result(node,group):
            map[group].add(node)
            for friend in graph[node]:
                if friend in map[group]:
                    return False
                # map[1-group].add(friend)
                if friend not in totalVisit:
                    totalVisit.add(friend)
                    if not result(friend,1-group):
                        return False
                    
            return True


        for i in range(1,n+1):
            if i not in totalVisit:
                totalVisit.add(i)
                mm = result(i,0)
                if not mm:
                        return False
                    
        return True

