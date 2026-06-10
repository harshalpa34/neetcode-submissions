class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq, tFreq= {}, {}

        for ch in s: 
            if ch in sFreq:
                sFreq[ch] += 1
            else:
                sFreq[ch] = 1
        
        
        for ch in t: 
            if ch in tFreq:
                tFreq[ch] += 1
            else:
                tFreq[ch] = 1

        return sFreq == tFreq

       