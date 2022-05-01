class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
                    break
                elif nums[i] < target and nums[i+1] > target:
                    return i + 1
        
        