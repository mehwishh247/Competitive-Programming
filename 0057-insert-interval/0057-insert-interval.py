class Solution:
            
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

#