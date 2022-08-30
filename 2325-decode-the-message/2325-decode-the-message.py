class Solution:
    
    def createDict(self, key):
        #remove spaces
        key = key.replace(" ", "")
        #turn key into an array
        array = [word for word in key]
        #keep only first occurence
        keep = []
        for letter in array:
            if letter not in keep: 
                keep.append(letter)
        #string for lower case alphabet
        alpha = list(string.ascii_lowercase)
        #create dict by zipping the key and values together
        dictionary = dict(zip(keep,alpha))
        #add spaces
        dictionary[' '] = ' '
        return dictionary
    
    def decodeMessage(self, key: str, message: str) -> str:
        dictionary = self.createDict(key)
        #remove spaces from message
        word = []
        for letter in message:
            new_letter = dictionary[letter]
            word.append(new_letter)
        word_clean = ''.join(word)
        return word_clean
            