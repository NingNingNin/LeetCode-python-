class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        lmax = [0]*len(height)
        rmax = [0]*len(height)

        lmax[0] = 0
        rmax[-1] = 0
        max1 = 0
        for i in range(1,len(height)):
            lmax[i] = max(height[i-1],max1)
            max1 = lmax[i]

        max1 = 0
        for i in range(len(height)-2,0,-1):
            rmax[i] = max(height[i+1],max1)
            max1 = rmax[i]

        result = 0

        for i in range(1,len(height)-1):
            if min(lmax[i],rmax[i])-height[i]>0:
              result = result + min(lmax[i],rmax[i])-height[i]
        
        print(lmax)
        print(rmax)

        return result


C = Solution()

height =[0,1,0,2,1,0,1,3,2,1,2,1]
Q = C.trap(height)
print(Q)