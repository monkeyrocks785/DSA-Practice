class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # for i in range(len(nums)):
        #     need = target - nums[i]
        #     if need in seen:
        #         return [seen[need], i]
        #     seen[num[i]] = i
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i