class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        result = []

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in mp.items():
            buckets[freq].append(num)

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result