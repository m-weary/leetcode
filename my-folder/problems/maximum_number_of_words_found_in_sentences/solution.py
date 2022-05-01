class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        split_sent = []
        word_count = []
        for i in range(len(sentences)):
            split_sent.append(sentences[i].split())
            count = len(split_sent[i])
            word_count.append(count)
        return max(word_count)