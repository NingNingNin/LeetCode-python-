class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums[:len(nums)-k] = reversed(nums[:len(nums) -k])
        nums[len(nums) -k:] = reversed(nums[len(nums) -k:])
        nums[:] = nums[::-1]    #nums[:] = reversed(nums)
                                #nums[:] = reversed(nums[:])  都可
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
Sol = Solution()
result = Sol.rotate(nums,k)
print(nums)
