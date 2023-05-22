class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
            n=len(s)

            ans=[]
            temp=[]

            def soln(idx):

                nonlocal temp

                if idx==n and len(temp)==4:
                    ans.append(".".join(temp))
                    return

                if idx>=n or len(temp)>4:
                    return


                if s[idx]=="0":
                    temp.append("0")
                    soln(idx+1)
                    temp.pop()
                    return

                for i in range(idx,n):
                    word=s[idx:i+1]

                    if int(word)>255:
                        break

                    temp.append(word)
                    soln(i+1)
                    temp.pop()



            soln(0)
            return ans
