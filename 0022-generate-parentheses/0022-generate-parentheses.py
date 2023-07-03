class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        combinations=[]
    
        def generateCombo(subs,openC,closeC):
            
            if openC==0 and closeC==0:
                combinations.append(subs)
                return
            if openC>0:
                generateCombo(subs+"(",openC-1,closeC)
            if closeC>openC:
                generateCombo(subs+")",openC,closeC-1)
        
        generateCombo("",n,n)
        
        return combinations
                
