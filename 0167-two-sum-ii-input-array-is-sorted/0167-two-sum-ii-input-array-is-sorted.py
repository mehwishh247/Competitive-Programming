class Solution:
    
    
     def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
            low,hi=0,len(numbers)-1
            
            while low<hi:
                summ=numbers[low]+numbers[hi]
                if summ==target:
                    return[low+1,hi+1]
                
                if summ<target:
                    low+=1
                else:
                    hi-=1
                    
                    
            
        
        
      
            
        