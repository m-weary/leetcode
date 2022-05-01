class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #First, find the last word
        #Calculate length of last word 
        if s.find(" ") == -1:
            return len(s)
        else:
            x = s.split()
            return len(x[-1])