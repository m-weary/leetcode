class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """Use a hashmap where the key is the indice and the value is the letter"""
        #conver the string to a list
        letters = [letter for letter in s]
        #Convert the values to a dict
        hm = dict(zip(indices,letters))
        #Sort the dict 
        hm = dict(sorted(hm.items()))
        #Join the values in the sorted order
        word = ''.join(hm.values())
        return word
            