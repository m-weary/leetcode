class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = OrderedDict.fromkeys(s,0) #create an ordered dictionary, using the list s as the keys
        for letter in s: #each time the letter shows up, add a count to the dict value
            hm[letter] = hm[letter] + 1
        #if the key for a letter has a value of 0, return it's index
        for letter in s:
            if hm[letter] == 1:
                return s.index(str(letter))
        return -1
        