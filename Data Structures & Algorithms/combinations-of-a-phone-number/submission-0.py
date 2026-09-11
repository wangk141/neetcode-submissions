class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alph = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        tmp = []
        
        def backtrack(i, curr):
            if len(curr) == len(digits):
                tmp.append(curr)
                return
            for a in alph[digits[i]]:
                backtrack(i + 1, curr + a)
            
        if digits:
            backtrack(0, "")
            
        return tmp