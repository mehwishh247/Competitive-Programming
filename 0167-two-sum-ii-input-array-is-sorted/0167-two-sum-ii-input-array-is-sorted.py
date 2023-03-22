class Solution:
    
    
     def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
            dic = defaultdict(int)
            
            
            
            for i,num in enumerate(numbers):
                
                if dic[target-num]:
                    j=dic[target-num]
                    return [j,i+1]
                
                dic[num]=i+1
                    
            
        
        
      
            
        