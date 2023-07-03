class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target = 12, position = [10, 8,  0, 5 ,3], speed = [2,4,1,1,3]
                                [12, 12, 1  6  6 ]     1   [2,4,1,1,1]
                                [        2  7  7 ]
                                
    ''' 
            
        pairs = [[p,s] for p,s in zip(position,speed)]
        
        pairs.sort()
        pairs = pairs[::-1]
        
        stack=[]
        
        for pair in pairs:
            
            time = (target-pair[0])/pair[-1]
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)
