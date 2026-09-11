class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st = {}
        for i in magazine:
            if i not in st:
                st.update({i : 1})
            else:
                st[i] += 1
        
        for j in ransomNote:
            if j not in st:
                return False
            st[j] -= 1
            if st[j] < 0:
                return False
        return True