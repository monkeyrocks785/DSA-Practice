class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # r = -inf
        # for i in range(len(nums)):
        #     cs = 0
        #     for j in range(i, len(nums)):
        #         cs += nums[j]
        #         r = max(r, cs)
        # return r

        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now