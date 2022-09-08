class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """The goal is to get the combined weight for each item"""
        #Create a set of all items
        items = items1 + items2
        #isolate a set of values
        values = []
        for item in items:
            values.append(item[0])
        values = set(values)
        #Create a dictionary with the values as the key and the weights as 0
        hm = dict.fromkeys(values,0)
        #Add the weight to the dictionary
        for item in items:
                hm[item[0]] += item[1]
        hm = dict(sorted(hm.items()))
        #Store the result in desired format
        res = []
        for key, value in hm.items():
            res.append([key,value])
        return res