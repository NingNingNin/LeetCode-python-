import copy

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def judge(l):
            length = len(l)
            for i in range(length//2):
                if l[i] != l[length-i-1]:
                    return False
            
            return True
        

        result = []
        res = []
        str = ""
 
        def search(str,res,epoch):
            if epoch > len(s)-1: return
            str = str + s[epoch]
            if judge(str):
                if  epoch == len(s)-1:
                    res.append(str)
                    res1 = copy.deepcopy(res)
                    result.append(res1)
                    if res:
                      res = res.pop()
                    return
                else:
                    search(str,res,epoch+1)
                    res.append(str)
                    search("",res,epoch+1)
                    if res:
                      res = res.pop()
            if not judge(str):
                    search(str,res,epoch+1)
                    

        search(str,res,0)
        return result                    


