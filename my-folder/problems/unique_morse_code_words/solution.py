class Solution:
    #Step 1, create a dictionary mapping morse:letter
    #Step 2, given the list words, convert each word to morse code
    #Use logic to evaluate how many words are written the same way in morse code.
        
    def createDict(self): #Step 1. Create the dict -> morse: letter
        morse_alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        letters = list(string.ascii_lowercase)
        dictionary = dict(zip(letters, morse_alpha))
        return dictionary
    
    def convertWords(self, dictionary, words):
        morse_output = [] #Create new list to store morse code translation
        for word in words: #iterate over each word
            morse_word = []
            for letter in word: #iterate over each letter
                morse_letter = dictionary[letter] #for each letter get the value
                morse_word.append(morse_letter) #join the morse values together
            morse_word = ''.join(morse_word) #concatenate the array
            morse_output.append(morse_word) #Put all of the words into an array
        return morse_output
        
    def uniqueTransformations(self, morse_output):
        unique_morse = set(morse_output)
        count = len(unique_morse)
        return count
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dictionary = self.createDict() 
        morse_output = self.convertWords(dictionary, words)
        count = self.uniqueTransformations(morse_output)
        return count
        
        