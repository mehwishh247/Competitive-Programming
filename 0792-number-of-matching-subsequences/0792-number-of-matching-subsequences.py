class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
            d = defaultdict(list)
            for i, c in enumerate(s):
                d[c].append(i)

            def is_subseq(word):
                index = -1
                for c in word:
                    i = bisect.bisect_left(d[c], index + 1)
                    if i == len(d[c]):
                        return False
                    index = d[c][i]
                return True
            x= sum(is_subseq(word) for word in words)
            return x