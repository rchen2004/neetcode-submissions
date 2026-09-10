class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count number of nums
        count = {}
        frequency = [[] for i in range (len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        
        for num, c in count.items():
            frequency[c].append(num)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res