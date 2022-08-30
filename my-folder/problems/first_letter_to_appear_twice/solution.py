class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """Create a dictionary with each letter as a key,
        iterate through the dictionary. For each letter, have the dict value be a counter. Once a value = 2, return the key"""
        hm = dict.fromkeys(set(s), 0) #Create dict
        for letter in s:
            hm[letter] += 1
            if hm[letter] == 2:
                return letter
        