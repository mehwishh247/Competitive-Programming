class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        
        n = len(ratings)

        lefts = [0,0]
        right = [0,0]

        count = 0

        for i in range(1,n-1):
            for j in range(n):
                if i==j:continue

                if j<i:

                    if ratings[j]<ratings[i]:
                        lefts[0]+=1
                    else:
                        lefts[-1]+=1
                else:

                    if ratings[j]<ratings[i]:
                        right[0]+=1
                    else:
                        right[-1]+=1
            
            count+=lefts[0]*right[-1] + lefts[-1]*right[0]
            lefts = [0,0]
            right = [0,0]

        return count



