class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = len(nums) * [1]
        right = len(nums) * [1]

 
        pre = 1
        for i in range(0,len(nums)):
            left[i] = nums[i] * pre
            pre = left[i]

        pre = 1
        for i in range(len(nums)-1,-1,-1):    #range(a,b),从a开始，到b前一个停止   第三个-1是步长
            right[i] = nums[i] * pre
            pre = right[i]

        result = len(nums)*[1]
        for i in range(1,len(nums)-1):
            result[i] = left[i-1] * right[i+1]
        result[0] = right[1]
        result[len(nums)-1] = left[len(nums)-2]
        return result
    

nums = [1,2,3,4]
Sol = Solution()
result1 = Sol.productExceptSelf(nums)
print(result1)
