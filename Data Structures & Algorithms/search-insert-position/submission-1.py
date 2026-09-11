class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            midpoint = (l + r)  // 2
            if nums[midpoint] > target:
                res = midpoint
                r = midpoint - 1
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                return midpoint
        return res
            