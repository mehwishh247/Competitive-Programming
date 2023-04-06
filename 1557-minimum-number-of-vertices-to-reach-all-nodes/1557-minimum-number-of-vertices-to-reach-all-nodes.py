class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
            graph_dic = defaultdict(list)
            for n1, n2 in edges:
                    graph_dic[n1].append(n2)
            ans = set()
            used=set()
            for i in range(n):
                stack = []
                if i in used:
                    continue 
                used.add(i)
                ans.add(i)
                stack.append(i)
                while stack:
                    out = stack.pop()
                    for j in graph_dic[out]:
                        if j in ans:
                            ans.discard(j)
                            continue
                        if j in used:
                            continue
                        else:
                            stack.append(j)
                            used.add(j)
            return ans