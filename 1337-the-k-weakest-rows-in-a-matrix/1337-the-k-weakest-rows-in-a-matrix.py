class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        counts = defaultdict(int)
        
        for row in range(len(mat)):
            cnt = Counter(mat[row])
            counts[row] = cnt[1]
            
        pos_answer = sorted(counts.items(), key=lambda x: (x[1], x[0]))
        answer = []
        
        for i in range(k):
            answer.append(pos_answer[i][0])
        
        return answer
    

                