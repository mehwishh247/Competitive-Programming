class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        sorted_score = list(x for _, x in sorted(zip(ages, scores)))
        sorted_age = sorted(ages)
        max_scores =  [sorted_score[0]]
        
        for i in range(1,n):
            curr = sorted_score[i]
            temp_max = 0
            for j in range(i):
                
                if sorted_score[j]<=curr:
                    temp_max = max(temp_max,max_scores[j])
                    
            max_scores.append(temp_max+curr)
                    
                    
                
        return max(max_scores)
                
        
                