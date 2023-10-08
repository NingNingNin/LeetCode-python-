class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        coloum = len(matrix[0])

        left,right = 0,row*coloum-1
        

        while left <= right:
            middle = (left+right)//2
            a,b  = middle//coloum , middle%coloum
            if matrix[a][b] == target:
                return True
            elif matrix[a][b] > target :
                right = middle - 1
            else:
                left = middle + 1

        return False
            
        



