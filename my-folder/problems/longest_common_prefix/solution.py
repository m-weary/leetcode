class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 1:
            result = strs[0]
        else:
            strs = sorted(strs)
            for i in range(len(strs[0])): #length of first word
                if strs[0][i] == strs[-1][i]:
                    result += strs[0][i]
                else:
                    break
        return result
    