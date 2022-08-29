class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Convert the number to a string, then join the list and convert to an integer
        num = int(''.join(map(str, digits)))
        #Add 1 to the number
        plus_one = num + 1
        #Convert back to string, and use list comprehension to put back into list
        plus_one = str(plus_one)
        final = [digit for digit in plus_one]
        return final
        