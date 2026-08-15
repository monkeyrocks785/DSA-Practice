class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        strs.sort()

        f = strs[0]
        l = strs[-1]
        j = 0

        while j < len(f) and j < len(l) and f[j] == l[j]:
            j += 1

        return f[:j]