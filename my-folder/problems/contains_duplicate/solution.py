class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #If a value appears twice, the set of nums will be a different length then the list
        if len(set(nums)) < len(nums):
            return True
        else:
            return False