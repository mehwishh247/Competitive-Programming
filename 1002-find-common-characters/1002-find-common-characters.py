class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
#         counts = []
        
#         for i in range(len(words)):
#             counts.append(Counter(words[i]))
#         myArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        
#         result = []
        
#         for chrt in myArray:
#             grt=0
#             for j in range(len(counts)):
#                 if counts[j][chrt]>0:
#                     grt+=1
#             if grt==len(counts):
#                 for j in range(counts[0][chrt]):
#                     result.append(chrt)
#         return result
            res = Counter(words[0])
            for a in words:
                res &= Counter(a)
            return list(res.elements())

