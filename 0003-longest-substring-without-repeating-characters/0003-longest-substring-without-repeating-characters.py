class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l = 0
        seen=set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[i])

            cur = i - l + 1
            ml = max(ml, cur)
    
        return ml