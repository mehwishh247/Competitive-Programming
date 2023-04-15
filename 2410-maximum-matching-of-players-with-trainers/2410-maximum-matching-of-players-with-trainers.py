class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        i,j,len1,len2 = 0,0,len(players),len(trainers)
        
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        
        ans=0
        while i<len1 and j<len2:
            if players[i]<=trainers[j]:
                ans+=1
                i+=1
                j+=1
            else:
                i+=1
        return ans
            
        
        