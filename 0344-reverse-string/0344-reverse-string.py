class Solution(object):
    def reverseString(self, s):
        i=0
        j=len(s)-1
        mid=(i+j)//2
        if len(s)%2==0:
            while i<=mid and j>=mid+1:
                t=s[i]
                s[i]=s[j]
                s[j]=t
                i+=1
                j-=1
            return s
        else:
            while i<mid and j>mid:
                t=s[i]
                s[i]=s[j]
                s[j]=t
                i+=1
                j-=1
            return s
      
            