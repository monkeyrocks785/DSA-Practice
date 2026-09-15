class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        mxl = 0
        l = 0

        for i in range(len(s)):
            ele = s[i]
            cnt[ele] = cnt.get(ele, 0) + 1

            while (i - l + 1) - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1

            wl = i - l + 1
            mxl = max(mxl, wl)

        return mxl