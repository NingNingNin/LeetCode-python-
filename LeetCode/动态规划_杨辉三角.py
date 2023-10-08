class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1],[1,1]]

        array = [[1]*numRows for _ in range(numRows)]


        for i in range(2,numRows):
            for j in range(1,i):
                array[i][j] = array[i-1][j] + array[i-1][j-1]

        result = []
        for i in range(numRows):
            result.append(array[i][0:i+1])

        return result


        

        