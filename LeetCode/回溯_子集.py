import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = []
        first = []
        res.append(first)

        for i in range(length):
            old_res = res[:]
            for result in old_res:
                 result1 =copy.deepcopy(result)
                 result1.append(nums[i])
                 res.append(result1)


        return res     