class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = ord('a')
    
        if len(s1) > len(s2):
            return False
        
        s1C, s2C = [0] *26, [0] * 26
        # check first lens1
        for i in range(len(s1)):
            s1C[ord(s1[i]) - a] += 1
            s2C[ord(s2[i]) - a] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1C[i] == s2C[i] else 0)
        # classic sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # check right pointer
            index = ord(s2[r]) - a
            s2C[index] += 1
            if s1C[index] == s2C[index]:
                matches += 1
            elif s1C[index] + 1 == s2C[index]:
                matches -= 1
            # check left pointer
            index = ord(s2[l]) - a
            s2C[index] -= 1
            if s1C[index] == s2C[index]:
                matches += 1
            elif s1C[index] - 1 == s2C[index]:
                matches -= 1
            
            l +=1
        return matches == 26