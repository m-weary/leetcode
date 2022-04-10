class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_rev = x[::-1]
        return x == x_rev