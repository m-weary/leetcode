class Solution:
    def sumZero(self, n: int) -> List[int]:
        """A key element of this question is the array can be any combination"""
        arr = [] #create an empty array
        sum_arr = 0 #track the sum of the array
        for i in range(1,n): #start the loop at 1 to eliminate edge case of n = 1 or 2
            val = i 
            arr.append(val)
            sum_arr += val
        arr.append(-(sum_arr)) #Add the inverse of the sum of the array as the last value 
        return arr
            