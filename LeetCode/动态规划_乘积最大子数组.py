class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        res = nums[0]
        maxnum = nums[0]
        minnum = nums[0]


        for i in range(1,length):
            nowmax = max(nums[i]*maxnum,nums[i]*minnum,nums[i])
            nowmin = min(nums[i]*maxnum,nums[i]*minnum,nums[i])
            res = max(nowmax,res)
            maxnum = nowmax
            minnum = nowmin

        return res