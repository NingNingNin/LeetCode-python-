import copy

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        leftnum,rightnum = n-1, n

        res = []
        str = "("

        def product(str,leftnum,rightnum):
            if leftnum ==0 and rightnum == 0:
                res.append(str)
                return
            if leftnum > 0:
                str = str + "("
                product(str,leftnum-1,rightnum)
                str = str[:-1]

            if rightnum >0 and rightnum > leftnum:
                str = str + ")"
                product(str,leftnum,rightnum-1)
                str = str[:-1]

        product(str,leftnum,rightnum)
        return res
                
                

