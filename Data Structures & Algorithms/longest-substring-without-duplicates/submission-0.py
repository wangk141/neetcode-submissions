class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_counter = 0
        tmp = ""
        while r < len(s):
            if s[r] not in tmp:
                tmp += s[r]
                r += 1
                max_counter = max(len(tmp), max_counter)
            else:
                tmp = tmp[1:]
                l += 1
        return max_counter


