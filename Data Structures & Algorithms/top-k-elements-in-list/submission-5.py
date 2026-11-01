class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for i, n in count.items():
            buckets[n].append(i)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for idx in buckets[i]:
                res.append(idx)
                if len(res) == k:
                    return res
            
            
        