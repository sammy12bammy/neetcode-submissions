class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''
        for s in strs:
            r += (str(len(s)))
            r += ('#')
            r += s
        return r

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = s.find('#', i)
            k = int(s[i:j])
            # Extract the word based on the length k
            word = s[j+1 : j+1+k]
            r.append(word)
            # move i to the start of the next length descriptor
            i = j + 1 + k
        return r