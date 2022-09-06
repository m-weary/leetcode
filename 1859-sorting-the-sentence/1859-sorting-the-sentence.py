class Solution:
    def sortSentence(self, s: str) -> str:
        """Since there is a limit of 9 words, we can use negative indexing to obtain the position"""
        #Convert the string into a list of words
        word_list = s.split()
        position_list = []
        words_clean = []
        for word in word_list:
            position_list.append(word[-1:])
            words_clean.append(word[:-1])
        #Create dict with the keys as position and the word as value
        hm = dict(zip(position_list, words_clean))
        hm= dict(sorted(hm.items()))
        return " ".join(hm.values())