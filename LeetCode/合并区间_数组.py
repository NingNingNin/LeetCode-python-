class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x: x[0])
        thefinal = [intervals[0]]

        for ob in range(1,len(intervals)):
            if intervals[ob][0] <= thefinal[-1][1]:
                thefinal[-1][1] = max(thefinal[-1][1],intervals[ob][1])
            
            else: thefinal.append(intervals[ob])
        
        return list(thefinal)