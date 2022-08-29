class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set(nums)
        for num in unique:
            if nums.count(num) == 1:
                return num