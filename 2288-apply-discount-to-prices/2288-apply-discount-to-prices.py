class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        
        sent = list(sentence.split(" "))
        
        for i in range(len(sent)):
            
            # print(sent[i], sent[i][1:],sent[i][-1].isnumeric())
            
            if sent[i][0]=="$" and sent[i][1:].isnumeric():
                price = float(sent[i][1:])
                result =format(price - (price* discount/100), ".2f")
                sent[i] = "$"+str(result)
        
        ans = " ".join(sent)

        
        return ans
        