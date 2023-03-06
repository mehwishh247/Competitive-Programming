class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx,i,j=0,0,0
        result=""
        while j<len(s):
            if s[j] in result:
                i+=1
                j=i
                result=""
            result+=s[j]
            j+=1
            maxx=max(maxx,j-i)
            
        return maxx
        
        
        

#         if len(s)==1:
#             return 1
#         maxx=0
        
#         for i,item in enumerate(s):
#             temp=[]
#             j=i+1
#             while j<len(s) and s[j] not in temp:
#                 temp.append(s[j])
#                 j+=1
#             length=j-i-1
#             maxx=max(length,maxx)
            
#         return maxx
            
        
            
        