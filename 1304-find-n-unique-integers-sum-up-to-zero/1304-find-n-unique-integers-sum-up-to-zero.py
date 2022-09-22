class Solution:
    def sumZero(self, n: int) -> List[int]:
        """A key element of this question is the array can be any combination"""
        arr = []
        sum_arr = 0
        for i in range(1,n):
            val = i
            arr.append(val)
            sum_arr += val
        arr.append(-(sum_arr))
        return arr
            