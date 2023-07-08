class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        ans = ""
        while a >= 1 and b>=1:
            if a-b>=1:
                ans = ans+"aab"
                a-=2
                b-=1
            elif a==b:
                ans += "ab"
                a-=1
                b-=1
            else:
                ans = ans+"bba"
                a-=1
                b-=2
            

        if a==2:ans += "aa"
        elif a==1 :ans += "a"
        if b==2 :ans += "bb"
        elif b==1:ans += "b"
        return ans