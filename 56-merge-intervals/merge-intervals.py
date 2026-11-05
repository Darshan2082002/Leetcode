class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged_intervals=[]
        current_start,current_end=intervals[0]
        for intervals_start,intervals_end in intervals[1:]:
            if current_end<intervals_start:
                merged_intervals.append([current_start, current_end])
                current_start, current_end = intervals_start, intervals_end
            else:
                current_end = max(current_end, intervals_end) 
        merged_intervals.append([current_start, current_end])  
        return merged_intervals
