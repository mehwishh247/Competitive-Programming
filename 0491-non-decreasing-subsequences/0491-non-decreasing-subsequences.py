class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
      
        
        answer=set()
        temp=[]
        n=len(nums)

        
        def solution(curr):
            


            if len(temp)>=2 and temp==sorted(temp):

                answer.add(tuple(temp))
    
    
            
            for i in range(curr,n):
                temp.append(nums[i])
                solution(i+1)
                temp.pop()
        
        solution(0)
        return answer
    
    
    
    