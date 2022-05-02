class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp = []
        halfway = int(len(nums)/2)
        for i in range(0,halfway):
            freq=nums[2*i]
            val=nums[2*i+1]
            result = [val]*freq
            decomp.append(result)
        final = []
        for i in decomp:
            final += i
        return final
            