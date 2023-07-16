class Solution:
    
    def findPosition(self,intervals,target):
        low,high=0,len(intervals)
        
        while low < high:
            mid=low + (high-low)//2
            if intervals[mid][0]<target:        
                low=mid+1
            else:
                high=mid
        return low
            
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        find the index of insertion using binary search
        '''
        merged = []
        i = 0

        # Add intervals that are completely before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged newInterval
        merged.append(newInterval)

        # Add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

#         indexS = self.findPosition(intervals,newInterval[0])
#         indexE = self.findPosition(intervals,newInterval[-1])


#         print(indexS,indexE)

#         n = len(intervals)     
        
        
#         if indexS>=1:
#             a,b = intervals[index-1]
#             startT,endT = newInterval 
            
        
        
        
        
        
        
        
        
        
        
        
#         if index>=1 and index<=n-1:
#             # check if its start is in its behind interval
#             a,b = intervals[index-1]
#             c,d = intervals[index] 
#             startT,endT = newInterval 
            
#             print(c,d,startT,endT)
#             if a <= startT <= b:
                
#                 if endT>b:
#                     intervals[index-1][-1] = endT
#                     return intervals

#             elif c <= startT <= d:

#                 if endT>d:
#                     intervals[index][-1] = endT
#                     return intervals


                

            
                
                
            
            
        
        
        return intervals
        
        
            