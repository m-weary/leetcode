class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        """Create a hashmap with the value as the key and the count as the value.
        If the count = 1, add the number to the sum"""
        hm={}
        for num in nums:
            if num in hm.keys():
                hm[num] += 1
            else:
                hm[num] = 1
        unique_sum = 0
        for key, value in hm.items():
            if value == 1:
                unique_sum += key
        return unique_sum