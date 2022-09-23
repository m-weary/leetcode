class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Convert each string to a sequential array of numbers, if the 
        array's match, the strings are isomorphic"""
        #convert each string to array
        arr_s = [i for i in s]
        arr_t = [i for i in t]
        #create hashmap for each 
        hm_s = {}
        counter = 0
        for i in arr_s:
            if i not in hm_s:
                hm_s[i] = counter
                counter += 1
        hm_t = {}
        counter = 0
        for i in arr_t:
            if i not in hm_t:
                hm_t[i] = counter
                counter += 1  
        #create new strings using hm
        arr_s_num = []
        arr_t_num = []
        for i in arr_s:
            val = hm_s[i]
            arr_s_num.append(val)
        for i in arr_t:
            val = hm_t[i]
            arr_t_num.append(val) 
        #Check to see if the arrays match
        if arr_s_num == arr_t_num:
            return True
        else:  
            return False
        