class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {1:                                              {'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'},
            2:{'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'},
            3:{'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'}}
        res = []
        for word in words:
            if word[0] in dic[1]:
                group = 1
            elif word[0] in dic[2]:
                group = 2
            else:
                group = 3
            print(word, group)
            for i in range(1, len(word)):
                if word[i] not in dic[group]:
                    break
            else:
                res.append(word)
        return res