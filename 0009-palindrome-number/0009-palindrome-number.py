class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = ""

        for i in x[::-1]:
            y+=i
        
        if x == y:
            return True
        
        return False