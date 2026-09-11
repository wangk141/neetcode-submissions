class Solution:
    def maxScore(self, s: str) -> int:
        def score(l, r):
            count = 0
            for i in range(len(l)):
                if l[i] == "0":
                    count += 1
            for j in range(len(r)):
                if r[j] == "1":
                    count += 1
            return count

        max_count = 0
        for i in range(len(s)):
            l = s[0:i+1]
            r = s[i+1:]
            if l == "" or r == "":
                break
            max_count = max(max_count, score(l, r))
        return max_count


        
        