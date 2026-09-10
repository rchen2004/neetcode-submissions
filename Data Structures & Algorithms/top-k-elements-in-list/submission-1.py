class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            frequent[num] = 1 + frequent.get(num, 0)
        
        arr = []
        for num, freq in frequent.items(): # value : frequency
            arr.append([freq, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


        