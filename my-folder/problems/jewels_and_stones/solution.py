class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        both = 0
        for stone in stones:
            if stone in jewels:
                both += 1
        return both
        
        
            
                