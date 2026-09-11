class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest, m):
            subarray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray <= m

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            # this is done to prevent overflow
            if canSplit(mid, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        
