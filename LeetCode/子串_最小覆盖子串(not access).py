class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t):
            return ""

        hash = {}
        flag = 0

        for i in range(len(t)) :
            hash[t[i]] = 0

        for i in range(len(t)) :
            hash[t[i]] += 1

        j = 0
        minlen = 100000
        right,left = 0,0
        for i in range(len(s)):
            if s[i] in hash :
                hash[s[i]] -= 1
            
            all_non_zero = True
            for value in hash.values():
                if value != 0:
                    all_non_zero = False
                    break
            
            while all_non_zero == True:
                if i - j +1 < minlen:
                   flag = 1
                   minlen = i - j +1
                   left = j
                   right = i
                
                if s[j] in hash:
                    hash[s[j]] += 1
                j += 1

                for value in hash.values():
                    if value != 0:
                        all_non_zero = False
                        break

        if flag ==1 :
           return s[left:right+1]
        else :return ""

                

            

            
