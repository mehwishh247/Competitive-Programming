class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        start=0
        end=len(skill)-1
        summ=skill[0]+skill[-1]
        result=0
        
        while start<end:
            if skill[start]+skill[end]==summ:
                result+=skill[start]*skill[end]
                start+=1
                end-=1
            else:
                return -1
            
        return result