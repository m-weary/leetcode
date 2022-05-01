class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Initialize the left a right pointer
        #The left pointer is for the index that we will store the unique values
        #The right pointer is for the index as we work through the array
        l = 1 #set at second point because the first will always be the same
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]: #compare to previous num in array, if it is different it is unique
                nums[l] = nums[r]
                l += 1
        return l
                