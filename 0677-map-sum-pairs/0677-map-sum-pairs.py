class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        
        for i,ltr in enumerate(key):
            
            idx = ord(ltr)-97
            
            if not curr.have[idx]:curr.have[idx] = TrieNode()
                
            curr = curr.have[idx]
        
        curr.is_end = True
        curr.value = val
        

    def sum(self, prefix: str) -> int:
        
        self.summ = 0
        
        curr = self.root
        for i,ltr in enumerate(prefix):
            
            idx = ord(ltr)-97
            
            if not curr.have[idx]: return self.summ
            
            curr = curr.have[idx]
        
        # print(curr.)
        def dfs(node):
            
            if not node: return
            if node.is_end:self.summ+=node.value
            
            for kids in node.have:
   
                dfs(kids)
        
        dfs(curr)
        return self.summ
                
            
            
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class TrieNode:
    def __init__(self):
        self.have = [None]*26
        self.is_end = False
        self.value = 0   