class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keyDefs = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

  
        ans = []
        def recur(array,idx):

            if len(array)==len(digits):
                ans.append("".join(array))
                return
            if idx==len(digits):
                return

            for ltr in keyDefs[digits[idx]]:

                array+=ltr
                recur(array,idx+1)
                array.pop()
        
        if len(digits)==0:
            return ans
        # n=len(digits)-1 if len(digits)>1 else 1 if len(digits)==1 else 0
        # for i in range(n):
        recur( [],0)
        
        return ans
            