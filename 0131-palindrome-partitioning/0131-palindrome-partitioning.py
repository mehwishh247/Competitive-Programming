class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp=[]
        answer=[]
        n=len(s)
    
        def dfs(index):
            if index == n:
                answer.append(temp[:])
                return
            for i in range(index,n):
                if s[index:i+1]==s[index:i+1][::-1]:
                    temp.append(s[index:i+1])
                    dfs(i+1)
                    temp.pop()
        dfs(0)
        return answer
            