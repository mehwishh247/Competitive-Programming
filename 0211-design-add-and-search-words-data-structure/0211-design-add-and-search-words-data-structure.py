class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        curr = self.root
        
        for c in word:
            curr = curr.kids[c]
        curr.is_end = True
        
    def search(self, word: str) -> bool:
       
        
        def src(ind,curr):
            
            
            if ind==len(word):
                return curr.is_end
                
            if word[ind]==".":
                ans = False
                for key in curr.kids:
                    ans |= src(ind+1,curr.kids[key])
                return ans
            
            if word[ind] not in curr.kids:
                return False
            
            return src(ind+1,curr.kids[word[ind]])
        
        
        curr = self.root
        return src(0,curr)
            
            
            

        
        
class TrieNode:
    
    def __init__(self):
        self.is_end=False
        self.kids=defaultdict(lambda: TrieNode())
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)