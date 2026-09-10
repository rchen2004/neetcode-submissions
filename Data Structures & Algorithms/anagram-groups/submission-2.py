class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # tells python if a key is accessed that doesn't exist, create it as a empty list
        for s in strs: # for every string
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())