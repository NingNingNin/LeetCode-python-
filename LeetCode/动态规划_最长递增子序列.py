class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        length = len(nums)


        s = [1]*length

        for i in range(length):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    s[i] = max(s[i],s[j]+1)


        return max(s)



