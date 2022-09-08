class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        #Combine the lists and find the set of the lists
        all_nums = nums1 + nums2 + nums3
        all_nums = set(all_nums)
        #Use these values as keys for a dictionary
        hm = dict.fromkeys(all_nums,0)
        #The value of dict for each key will show how many lists it appears in
        for num in set(nums1):
            if num in hm.keys():
                hm[num] += 1
        for num in set(nums2):
            if num in hm.keys():
                hm[num] += 1
        for num in set(nums3):
            if num in hm.keys():
                hm[num] += 1
        res = []
        for key, val in hm.items():
            if val >= 2:
                res.append(key)
        return res     