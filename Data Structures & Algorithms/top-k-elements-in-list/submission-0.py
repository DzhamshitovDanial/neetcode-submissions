class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        for i in nums:
            if i not in dct:
                dct[i]=0
            dct[i]+=1
        unique_elements = sorted(dct.keys(), key=dct.get, reverse=True)
        return unique_elements[:k]
    