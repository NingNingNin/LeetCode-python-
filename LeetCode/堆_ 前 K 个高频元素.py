import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hash = {}
        result = []

        for i in nums :
            if i not in hash :
                hash[i] = 1
            else : hash[i] += 1
        hash = sorted(hash.items(),key=lambda x : x[1])
        for i in range(1,k+1):
           result.append(hash[-i][0])

        return result