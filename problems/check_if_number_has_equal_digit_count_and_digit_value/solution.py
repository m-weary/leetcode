class Solution:
    def digitCount(self, num: str) -> bool:
        #If the string is one value long, return false
        if len(num) == 1: return False

        cnt = {}
        i = 0
        
        while i < len(num):
            cnt[i] = num.count(str(i))
            i += 1
            
        for i in range(len(num)):
            print(num[i], cnt[i])
            if num[i] != str(cnt[i]):
                return False
        return True