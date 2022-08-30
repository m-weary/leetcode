class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0 #left pointer
        r = len(s) - 1 #right pointer
        
        while l < r:
            s[l], s[r] = s[r], s[l] #Swap first with last, and last with first
            l += 1 #move left pointer up
            r -= 1 #move right pointer back
            
        
            