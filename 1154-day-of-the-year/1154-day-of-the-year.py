class Solution:
    def dayOfYear(self, date: str) -> int:
        
        
        month_days = {1: 31,2: 28,3: 31, 4: 30,5: 31, 6: 30, 7: 31, 8: 31, 9: 30,10: 31, 11: 30, 12: 31 }
        
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            month_days[2] =29
        
        ans = day
        for i in range(1,month):
            ans+=month_days[i]
            
        return ans
