class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False
        self.indexes = []

class Trie:

    def __init__(self):
        self.root = Node()
    
    def charToIndex(self, char):
        return ord(str(char)) - 97
    
    def indexToChar(self, index):
        return chr(index + 97)

    def reachNode(self, value, root = None):
        curr = root if root else self.root
        parent, index = curr, -1
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                return (None, None, -1)
            parent = curr
            curr = curr.child[index]
        return (curr, parent, index)
 
    def insert(self, value, weight) -> None:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr.indexes.append(weight)
            curr = curr.child[index]
        curr.end = True
        curr.indexes.append(weight)
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()
        for i, word in enumerate(words):
            self.prefix.insert(word, i)
            self.suffix.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        prefix = self.prefix.reachNode(pref)[0]
        suffix = self.suffix.reachNode(suff[::-1])[0]
        prefix = [] if not prefix else prefix.indexes
        suffix = [] if not suffix else suffix.indexes
        n, m = len(prefix) - 1, len(suffix) - 1
        while n >= 0 and m >= 0:
            if prefix[n] == suffix[m]:
                return prefix[n]
            elif prefix[n] > suffix[m]:
                n -= 1
            else:
                m -= 1
        return -1
        
