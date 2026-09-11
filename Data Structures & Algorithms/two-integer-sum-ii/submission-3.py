class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary(numbers: List[int], target: int, i: int) -> int:
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                midpoint = (left + right) // 2
                if numbers[midpoint] < target:
                    left = midpoint + 1
                elif numbers[midpoint] > target:
                    right = midpoint - 1
                else:
                    return midpoint
            return -1

        for i in range(len(numbers)):
            res = target - numbers[i]
            result = binary(numbers, res, i)
            if result != -1:
                return [i + 1, result + 1]