class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        resultHashMap = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            resultHashMap[tuple(count)].append(s)
        
        return resultHashMap.values()