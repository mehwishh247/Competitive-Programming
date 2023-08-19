class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n=len(intervals)
        result = [intervals[0]]
        
        for i in range(1,n):
            
            start,end = intervals[i]
            
            if start>result[-1][-1]:
                    result.append(intervals[i])
            else:
                
                result[-1][-1] = max(result[-1][-1],end)

            
        return result

        