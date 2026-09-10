class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key -> multiple values

        for s in strs:
            sortedS = ''.join(sorted(s)) # sort the string but it is a list object, so you use join to convert it into a string
            res[sortedS].append(s) # since anagrams sorted would be the same, store the value using the sorted value as key
        return list(res.values()) # return the dictionary object as a list
        