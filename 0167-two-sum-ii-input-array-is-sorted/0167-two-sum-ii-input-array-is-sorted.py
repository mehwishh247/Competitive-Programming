class Solution:
    
    
     def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
            '''
                    [2,7,7,11,13,14,14,15]   21
                       i              j
            
            '''
            n = len(numbers)
            l,r, = 0,n-1
            
            while l<r:
                
                curr_sum = numbers[l]+numbers[r]
                
                if curr_sum == target: return [l+1,r+1]
                
                if curr_sum>target: r -= 1
                else: l += 1
                    
            return []
            