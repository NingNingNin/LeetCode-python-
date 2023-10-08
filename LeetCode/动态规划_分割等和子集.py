class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2==1: return False

        row = len(nums)
        colomn = sum(nums)//2

        dp = [[False]*(colomn+1) for _ in range(row+1)]


        for i in range(1,row+1):
            for j in range(0,colomn+1):
                if nums[i-1] == j :
                    dp[i][j] = True
                elif nums[i-1] > j :
                    dp[i][j] = dp[i-1][j]
                else :
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        
        return dp[row][colomn]