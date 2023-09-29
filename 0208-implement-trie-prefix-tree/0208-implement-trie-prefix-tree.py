class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            curr = curr.kids[c]
        curr.is_end = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:           
            if c not in curr.kids:
                return False
            curr = curr.kids[c]
        return curr.is_end
            
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:           
            if c not in curr.kids:
                return False
            curr = curr.kids[c]
        return True
        

        
class TrieNode:
    def __init__(self):
        self.is_end  = False
        self.kids = defaultdict(lambda: TrieNode())


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)