class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l = 0
        seen={}

        for i in range(len(s)):
            ele = s[i]
            if ele in seen:
                l = max(l, seen[ele] + 1)
            
            seen[ele] = i

            cur = i - l + 1
            ml = max(ml, cur)
    
        return ml