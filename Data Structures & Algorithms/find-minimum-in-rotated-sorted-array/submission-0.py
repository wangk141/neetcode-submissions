class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = left + (right - left) // 2
            if nums[midpoint] < nums[right]:
                right = midpoint
            else:
                left = midpoint + 1
        return nums[midpoint]
            
