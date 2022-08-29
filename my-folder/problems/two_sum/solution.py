class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Can use a hashmap. Map Value to Index
        hm = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hm:
                return [hm[diff],index]
            else:
                hm[value] = index
            
        
        
                
                