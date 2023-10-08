class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) -1

        max1 = (j - i) * min(height[i],height[j])

        while i < j :
            if height[i] < height [j]:
                max1 = max(max1,(j-i-1) * min(height[i+1],height[j]))
                i = i +1
            else : 
                max1 = max(max1,(j-i-1) * min(height[i],height[j-1]))
                j = j -1

        return max1




        