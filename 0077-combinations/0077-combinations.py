class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=set()
        temp=[]
        n+=1

        
        def solution(curr):
            temp.append(curr)
#             prepare your answer here
            if len(temp)>=k:
                answer.add(tuple(temp[len(temp)-k:]))
            if curr==n-1:
                return
            
            for i in range(curr+1,n):
                solution(i)
                temp.pop()
                
        solution(1)
        return list(answer)
            
            
            
        
        
        