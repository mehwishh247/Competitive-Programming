class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=[]
        i=0
        j=len(people)-1
        people=sorted(people)
        while i<=j:
            if people[i]+people[j]<=limit:
                boat.append([people[i],people[j]])
                i+=1
                j-=1
            elif people[j]<=limit:
                boat.append([people[j]])
                j-=1
        return len(boat)
                


