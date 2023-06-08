class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        possible_ans = defaultdict(list)
        
        label = 1
        
        up = True
        
        for i in range(len(s)):
            possible_ans[label].append(s[i])

            if up:
                label+=1
            else:
                label-=1
            
            if label==numRows:
                up = False
            if label ==1:
                up=True
                
        result = ''
        
        for key in possible_ans.keys():
           result+= "".join(possible_ans[key])
        
        return  result
                
                
            
                
            