class Solution:
    def getRow(self, n: int):
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        result = [1]
        
        recArr = self.getRow(n-1)

        for i in range(n-1):
            summ = recArr[i]+recArr[i+1]
            result.append(summ)
        result.append(1)
        return result

    
    
    def generate(self, numRows: int) -> List[List[int]]:
        
        allRes = []
        for i in range(numRows):
            allRes.append(self.getRow(i))
            
        return allRes
            
        
            
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
