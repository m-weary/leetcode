class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #Set up the variables we will need to track altitude
        max_alt = 0 
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            max_alt = max(max_alt, alt)
        return max_alt