class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = heights.copy()
        sorted_h.sort()

        counter = 0
        for i in range(len(heights)):
            if heights[i] != sorted_h[i]:
                counter += 1
        return counter