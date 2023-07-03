class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        a = (num-3)/3
        
        if not a.is_integer():
            return []
        
        return [int(a),int(a+1),int(a+2)]
        
        
        
        
 