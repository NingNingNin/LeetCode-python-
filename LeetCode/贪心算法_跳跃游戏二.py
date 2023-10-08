class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        index = 0
        max_pos = 0
        max_step = 0

        while index < len(nums) - 1:
            max_pos = max(max_pos, index + nums[index])
            if index == max_step:
                count += 1
                max_step = max_pos
            index += 1

        return count