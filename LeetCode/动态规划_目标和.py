class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        f = [[0]*(target+1)  for _ in range(len(nums)+1)]
        f[0][0] = 1

        for i in range(1,len(nums)+1):
            for j in range(0,target+1):
                if nums[i-1]>j : f[i][j] = f[i-1][j]
                else : f[i][j] = f[i-1][j] + f[i-1][j-nums[i-1]]

        return f[len(nums)][target]
        