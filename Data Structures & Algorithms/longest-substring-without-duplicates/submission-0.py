class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curMax = 0
        st = set()
        
        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                r += 1
                curMax = max(r -l , curMax)
                continue

            while s[l] != s[r]: 
                st.remove(s[l])
                l += 1
            
            st.remove(s[l])
            l += 1
            st.add(s[r])
            r += 1
            curMax = max(r-l, curMax)

        return curMax
                