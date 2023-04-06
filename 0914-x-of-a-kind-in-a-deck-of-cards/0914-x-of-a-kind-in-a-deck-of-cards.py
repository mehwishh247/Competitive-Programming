class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        cur_gcd=cnt[deck[0]]
        for key in cnt.keys():
            cur_gcd = math.gcd(cur_gcd,cnt[key])
            if cur_gcd==1:
                return False
        return True