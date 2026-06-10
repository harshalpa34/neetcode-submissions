class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        subStr = "";
        maxlen = len(subStr)
        while (r < len(s)):
            if s[r] not in subStr:
                subStr += s[r]
                maxlen = max(maxlen, len(subStr))
                print(subStr)
            elif s[r] in subStr:
                subStr = subStr[1:]
                l += 1
                continue;
            r+=1;
        return maxlen 

