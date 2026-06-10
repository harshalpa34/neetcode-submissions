class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anag.keys():
                print(sortedWord)
                anag[sortedWord].append(word) 
            else: 
                anag[sortedWord] = [word];
            
        return list(anag.values())