class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        questions[-1] = questions[-1][0]
        
        currMax = questions[-1]
        
        for i in range(n-2,-1,-1):
            
            mark,jump = questions[i]
            nextPossible = i+jump+1
            
            if nextPossible<n:
                mark += questions[nextPossible]

            currMax = max(currMax,mark)
            questions[i] = currMax
        
        return questions[0]
            
                
                
            
                
            
            
        
        
        