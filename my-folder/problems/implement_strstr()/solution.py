class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = len(needle)
        k=-1
        if len(needle) == 0:
            k = 0
        elif len(haystack) == 1:
            if haystack == needle:
                k=0 
        elif len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    k = i
                    break
        elif len(haystack) == len(needle):
            if haystack == needle:
                k=0 
        else:
            for i in range(len(haystack)):
                if haystack[i:i+x] == needle:
                    k = i
                    break
        return k
            
        
        