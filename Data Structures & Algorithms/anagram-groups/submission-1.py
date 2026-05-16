class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in dct:
                dct[s]=[]
            dct[s].append(i)
        return list(dct.values())
            