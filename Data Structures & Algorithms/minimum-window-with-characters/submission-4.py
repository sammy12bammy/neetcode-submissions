class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, curWindow = {},{}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
            
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l=0

        for r in range(len(s)):
            c = s[r]
            curWindow[c] = 1 + curWindow.get(c, 0)

            if c in countT and curWindow[c] == countT[c]:
                have += 1
                
            while have == need:
                # size of cur window
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                # pop from left
                curWindow[s[l]] -= 1
                if s[l] in countT and curWindow[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        