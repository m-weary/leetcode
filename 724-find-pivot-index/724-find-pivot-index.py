class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Use a for loop to iterate through the array
        #If the leftSum == rightSum, return the index
        leftSum = 0
        rightSum = sum(nums)
        for i in range(len(nums)):
            if i > 0:
                leftSum += nums[i - 1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
                break
        return -1
            