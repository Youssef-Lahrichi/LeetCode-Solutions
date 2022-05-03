class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0: return False
        else:
            x = str(x)
            if x[:(len(x)-1)/2] == x[(len(x)+1)/2:len(x)][::-1]:
                return True
            elif x[:len(x)/2] == x[len(x)/2:len(x)][::-1]:
                return True
        return False
                
