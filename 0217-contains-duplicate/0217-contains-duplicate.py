class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # mp = {}
        # for i in nums:
        #     if i not in mp:
        #         mp[i] = 1
        #     else:
        #         mp[i] += 1
        # for i in mp:
        #     if mp[i] > 1:
        #         return True
        # return False

        mp = set()
        for i in nums:
            if i in mp:
                return True
            else:
                mp.add(i)
        return False