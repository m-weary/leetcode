class Solution:
    
    def __init__(self):
        self.rods = {} #Create a dict with keys for each ring position
        for i in range(0,10): #for each position betwenn 0 and 9
            self.rods[i] = [] #Make each of the positions an empty list
            
    def countPoints(self, rings: str) -> int:
        count = 0
        for i in range(0,len(rings), 2): #for every letter
            letter = rings[i]
            rod = int(rings[i+1])
            self.rods[rod].append(letter)
        for key, value in self.rods.items():
            if 'B' in value and 'G' in value and 'R' in value:
                count += 1
        return count
        
            

        
        
            
            
        
        