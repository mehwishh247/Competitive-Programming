class Solution:
    def reverseWords(self, s: str) -> str:
        
        answer = ""
        raw = s.split(" ")
        
        for i in range(len(raw)-1,-1,-1):
            
            if raw[i]:
                answer+=" "+raw[i]
        
        return  answer[1:]