class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #Convert both lists to strings
        word_1_str = "".join(word1)
        word_2_str = "".join(word2)
        if word_1_str == word_2_str:
            return True
        else:
            return False