class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """Check if all characters in each word appear in the string allowed """
        count = 0
        for word in words:
            # if the set of each word is a subset of the letters in allowed
            if set(word).issubset(allowed):
                count += 1        
        return count