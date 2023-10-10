class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i,ltr in enumerate(word):
            idx = ord(ltr)-97
            if not curr.have[idx]:
                curr.have[idx] = TrieNode()
            curr = curr.have[idx]
            
        curr.is_end = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for i,ltr in enumerate(word):
            idx = ord(ltr)-97
            if not curr.have[idx]: return False
            
            curr = curr.have[idx]
        return curr.is_end
            
            
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i,ltr in enumerate(prefix):
            idx = ord(ltr)-97
            if not curr.have[idx]: return False
            
            curr = curr.have[idx]
        return True
            
        

        
class TrieNode:
    def __init__(self):
        self.have = [None]*26
        self.is_end = False
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)