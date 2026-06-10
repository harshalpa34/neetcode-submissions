class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        res =[]  
        for i in nums:
            if i in freq.keys():
                freq[i] += 1
            else: 
                freq[i] = 1;
        print(freq)
        for i in range(0, k):
            maxFreq = {"freq": 0, "n": 0}
            for num in freq.keys():
                if freq[num] > maxFreq["freq"]:
                    maxFreq["freq"] = freq[num]
                    maxFreq["n"] = num
            del freq[maxFreq["n"]]
            res.append(maxFreq["n"])
        return res

        