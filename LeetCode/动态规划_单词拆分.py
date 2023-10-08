class Solution(object):
    def __init__(self) :
        self.flag = False
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        flag = [False] * (len(s)+1)
        flag[0] = True

        for i in range(len(s)):
            for j in range(0,i+1):
                if flag[j] == True and s[j:i+1] in wordDict:
                    flag[i+1] = True

        
        return flag[-1]



                