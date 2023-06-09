class RandomizedSet:

    def __init__(self):

        self.seen = defaultdict(int)
        self.seet = set()

    def insert(self, val: int) -> bool:

        if not self.seen[val]:
            self.seen[val]+=1
            self.seet.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        
        if self.seen[val]:
            self.seen[val]-=1   
            self.seet.discard(val)
            return True        
        return False

    def getRandom(self) -> int:
        
        arr = list(self.seet)
        
        if len(arr) != 0:
            random_index = random.randint(0, len(arr) - 1)
            return arr[random_index]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()