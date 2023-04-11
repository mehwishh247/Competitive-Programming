"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.summ=0
        
        def finder(ID):
            for employe in employees:            
                if employe.id==ID:
                    return employe
        
        def dfs(employe):
            self.summ += employe.importance
            if not employe.subordinates:
                return
            
            for child in employe.subordinates:
                x = finder(child)
                dfs(x)
                
            
                

        starter = finder(id)
        dfs(starter)
        return self.summ
       
