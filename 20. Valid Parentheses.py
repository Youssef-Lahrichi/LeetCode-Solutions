class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        sets = {")":"(", "]":"[", "}":"{"}
        
        stack = []
        
        for p in s:
            if p in sets:
                if len(stack) == 0:
                    return False
                elif sets[p] != stack.pop(len(stack)-1):
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0
