class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        answer = ""
        
        for word in words:
            
            if trie.search(word):
                if len(answer)==len(word):
                    answer = min(word,answer)
                else:
                    answer = word if len(word)>len(answer) else answer
        
        return answer
                

            
        
        
        
        
        
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self,word):
        curr = self.root
        
        for i,ltr in enumerate(word):
            
            idx = ord(ltr)-97
            
            if not curr.have[idx]:curr.have[idx] = TrieNode()
                
            curr = curr.have[idx]
        
        curr.is_end = True
    
    def search(self,word):
        
        curr = self.root
        
        for i,ltr in enumerate(word):
            
            idx = ord(ltr)-97
            
            if not curr.have[idx].is_end: return False
            curr = curr.have[idx]
            
        return True
        
      
    
    
        
        
class TrieNode:
    def __init__(self):
        self.have = [None]*26
        self.is_end = False  