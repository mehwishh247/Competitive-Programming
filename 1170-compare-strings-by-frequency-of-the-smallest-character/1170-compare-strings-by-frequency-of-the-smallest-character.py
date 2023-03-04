class Solution:
    def fser(self,array):
        fsList =[]
        for word in array:
            word=sorted(word)
            cnt = Counter(word)
            fsList.append(cnt[word[0]])
        return fsList
    def posTell(self,nums,target):
        low,high=-1,len(nums)
        while low+1<high:
            mid=low + (high-low)//2
            if nums[mid]>target:
                 high=mid
            else:
                low=mid
        return high
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        querFs = self.fser(queries)
        wordFs = sorted(self.fser(words))
        result=[]
        for qFS in querFs:
            pp = self.posTell(wordFs,qFS)
            grter = len(wordFs)-pp
            result.append(grter)
        return result