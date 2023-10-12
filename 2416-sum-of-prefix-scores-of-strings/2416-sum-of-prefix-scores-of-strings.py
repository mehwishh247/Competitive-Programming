class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        tri = Trie()
        
        for word in words:
            tri.insert(word)
        result = []
        for word in words:
            result.append(tri.score(word))
        return result
        

        
class TrieNode:
    def __init__(self):
        self.have = [None]*26
        self.pc = 0
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        
        curr = self.root
        for i,ltr in enumerate(word):
            
            idx = ord(ltr)-97
            
            if not curr.have[idx]: 
                curr.have[idx] = TrieNode()
            
            curr.have[idx].pc+=1
            curr = curr.have[idx]
            
        
    def score(self,word):
        
        summ = 0
        curr = self.root
        
        for i,ltr in enumerate(word):
            
            idx = ord(ltr)-97
            
            summ+= curr.have[idx].pc
            
            curr = curr.have[idx]
        return summ
            