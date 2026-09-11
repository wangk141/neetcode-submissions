class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = ""
        r = 0
        maxLen = 0
        while r < len(s):
            if s[r] not in st:
                st += s[r]
                maxLen = max(len(st), maxLen)
                r += 1
            else:
                st = st[1:]
        return maxLen