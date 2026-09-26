class Solution:
    def rob(self, nums: list[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        def rob_lin(arr):
            p1 = 0
            p2 = 0

            for i in arr:
                cur = max(p1, i + p2)

                p2 = p1
                p1 = cur

            return p1

        return max(rob_lin(nums[:-1]), rob_lin(nums[1:]))