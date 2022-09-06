class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """Convert the string to an list where each word is an element
        Restrict the list to only k elements (index will be k-1)
        Convert the list back to a string"""
        
        #Use split() to convert the sentence to an array
        ls = s.split()
        #Restrict it to the kth element
        words = ls[:k]
        #Convert back to string
        output = " ".join(words)
        #Return the output
        return output