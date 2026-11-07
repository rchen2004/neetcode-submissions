class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0
        prevSum = {0 : 1}

        for num in nums:
            curSum += num
            res += prevSum.get(curSum - k, 0)
            prevSum[curSum] = prevSum.get(curSum, 0) + 1
        return res