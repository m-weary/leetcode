class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Brute force
        max_prod = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = (nums[i]-1)*(nums[j]-1)
                max_prod = max(max_prod, prod)
        return max_prod"""
        #More eloquent. The max product will always be between the top two values in the array
        nums_sort = sorted(nums)
        #Calculate the product of the last two values
        return (nums_sort[-2]-1)*(nums_sort[-1]-1)