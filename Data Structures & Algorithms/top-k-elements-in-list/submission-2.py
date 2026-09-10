class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            frequent[num] = 1 + frequent.get(num, 0)
        
        arr = []
        for num, freq in frequent.items(): # value : frequency
            arr.append([freq, num]) # freq is the primary value so its sorted based on that
        arr.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res


        