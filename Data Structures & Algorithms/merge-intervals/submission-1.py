class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = [intervals[0]]

        for i in intervals[1:]:
            currstart, currend = i
            prevstart, prevend = merged[-1]

            if currstart <= prevend:
                merged[-1][1] = max(currend, prevend)
            else:
                merged.append(i)

        return merged