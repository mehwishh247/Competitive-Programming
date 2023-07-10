class Solution:
    def baseNeg2(self, n: int) -> str:
        
        if n==0:return '0'

        result = ""

        while n!=0:
            remain = n% -2
            n //=-2   
            if remain<0:
                remain+=2
                n+=1
            result = str(remain)+result

        return result
