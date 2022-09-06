class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """Use counters to count the number of R's and number of Ls"""
        r_count=0
        l_count=0
        count=0
        for i in s:
            if i == 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                count += 1
        return count
            