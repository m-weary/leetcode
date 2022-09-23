class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #if s is longer than t, it cannot be a subsequence
        if len(s) > len(t):return False
        if len(s) == 0:return True
        #Set a pointer starting at index 0
        subsequence=0
        #Iterate through t
        for i in range(0,len(t)):
            #If the pointer is within range of s
            if subsequence <= len(s) -1:
                print(s[subsequence]) #print the character we are looking at
                if s[subsequence]==t[i]: #If the character we ate looking comes sequentially in t, then increase the counter by 1

                    subsequence+=1
        #once we have gone through the loop, subsequence should be the len of s
        return  subsequence == len(s) 