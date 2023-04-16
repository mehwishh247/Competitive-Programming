class Solution:

    def lastApear(self,ltr,s):
        for i in range(len(s)-1,-1,-1):
            if s[i]==ltr:
                return i
        return -1

    def partitionLabels(self, s: str) -> List[int]:


        cur_max = float('-inf')
        idx = 0
        ans=[]
        while idx<len(s):
            last = self.lastApear(s[idx],s)
            cur_max = max(cur_max,last)
            if idx==cur_max:
                ans.append(idx-sum(ans)+1)
            idx+=1
        
        
        return ans