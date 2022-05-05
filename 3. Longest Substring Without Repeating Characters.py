class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        maxi = 0
        
        seen = set()
        while j < len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                maxi = max(maxi, len(seen))
                j += 1
        return maxi
