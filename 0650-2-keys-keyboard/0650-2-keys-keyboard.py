class Solution:
    def minSteps(self, n: int) -> int:
        
        mastawesha = defaultdict(lambda:-1)
        
        def dfs(screen,clipboard,steps):
            
            pos =  mastawesha[(screen,clipboard,steps)]
            
            if pos != -1: return pos
            
            if len(screen)==n: return steps
            
            if len(screen)>n: return float('inf')
            
            copy = paste = float('inf')
            
            if len(clipboard) != 0:
                paste = dfs(screen+clipboard,clipboard,steps+1)
            
            if len(clipboard) != len(screen):
                copy = dfs(screen,screen,steps+1)
            
            melse = min(copy,paste)
            mastawesha[(screen,clipboard,steps)] = melse
            
            return melse 
                

        
            
        return dfs("A","",0)

       