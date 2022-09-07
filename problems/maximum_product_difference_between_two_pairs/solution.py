class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        """I am assuming that we always want to use the two largest numbers in the first pair, and the two smallest numbers in the second pair
        Step 1. Order the list
        Step 2. Assign the first pair to the values at index -1 and -2
        Step 3. Assign the second pair to the values at index 0 and 1
        Step 4.Calculate the product difference"""
        nums_ordered = sorted(nums)
        print(nums_ordered)
        sum_high = nums_ordered[-2] * nums_ordered[-1]
        sum_low = nums_ordered[0] * nums_ordered[1]
        max_prod_dif = sum_high - sum_low
        return max_prod_dif
        