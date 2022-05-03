class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        num = 0
        i = 0
        while i < len(s) - 1:
            if mapping.get(s[i]) < mapping.get(s[i+1]):
                num += mapping.get(s[i+1]) - mapping.get(s[i])
                i+=2
            else:
                num += mapping.get(s[i])
                i+=1
        if i < len(s):
            num += mapping.get(s[i]) 
        return num
        
