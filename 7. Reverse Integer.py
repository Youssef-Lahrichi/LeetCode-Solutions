class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31: return 0 
        else:
            x = str(x)
            if x[0] != '-':
                if int(x[::-1]) >= 2**31-1:
                    return 0
                else:
                    return int(x[::-1])
            else:
                x = x[1:]
                if int('-'+(x[::-1])) <= -2**31: return 0
                else:
                    return int('-'+(x[::-1]))
