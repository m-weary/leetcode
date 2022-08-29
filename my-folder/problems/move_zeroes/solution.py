class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 #index
        c = 0 #counter
        while 0 in nums:
            #If not 0, move to next
            if nums[i] != 0:
                i += 1
            #If 0, delete it and keep count of it
            else:
                del(nums[i])
                c += 1
        for i in range(c):
            nums.append(0)
            
            