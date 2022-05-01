class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            running_sum.append(running)
        return running_sum