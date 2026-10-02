class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        dif = arr[1] - arr[0]
        a = 0
        b = 1

        while b < len(arr):
            d = arr[b] - arr[a]
            if d != dif:
                return False
            
            b += 1
            a += 1

        return True