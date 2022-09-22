class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        currentSum = 0
        for i in nums:
            currentSum += i
            runningSum.append(currentSum)
        return runningSum