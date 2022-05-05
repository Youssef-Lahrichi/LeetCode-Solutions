class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        curr = ''
        for i in range(len(min(strs, key=len))):
            letter = strs[0][i]
            for str in strs:
                if str[i] != letter:
                    return curr
            curr += letter
        return curr
