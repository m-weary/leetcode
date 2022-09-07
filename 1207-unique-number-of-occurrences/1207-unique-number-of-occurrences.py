class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """Create a dict with the key as a unique value, value as the counter
        If the value is in the dict, increase the counter by 1
        if not, add the value to the dict and add 1
        At the end of the loop, check the values"""
        hm = {}
        for num in arr:
            if num in hm.keys():
                hm[num] += 1
            else:
                hm[num] = 1
        #Check if any of the values are the same
        vals = list(hm.values())
        if sorted(vals) == sorted(list(set(vals))):
            return True
        else:
            return False


