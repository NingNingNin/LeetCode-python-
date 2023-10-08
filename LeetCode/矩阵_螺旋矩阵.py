class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        list = [(0,1),(1,0),(0,-1),(-1,0)]
        flag = 0
        res = []
        number = len(matrix)*len(matrix[0])
        isvisit = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        i,j = 0,0
        isvisit[0][0] = 1
        while number > 0:
            res.append(matrix[i][j])
            k,l = list[flag]
            i = i + k
            j = j + l
            if not 0<=i<len(matrix) or not 0<=j<len(matrix[0]) or isvisit[i][j] == 1:
                i = i - k
                j = j - l
                flag = (flag+1) % 4
                k,l = list[flag]
                i = i + k
                j = j + l
            isvisit[i][j] = 1
            number -= 1
        
        return res