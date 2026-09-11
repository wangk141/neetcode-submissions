class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actual_k = k % len(nums)
        print(actual_k)

        for _ in range(k):
            nums.insert(0, nums.pop())