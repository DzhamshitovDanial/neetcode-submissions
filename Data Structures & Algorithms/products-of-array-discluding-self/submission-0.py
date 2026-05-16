class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            nn=nums[:]
            del nn[i]
            total=1
            for j in range(len(nn)):
                    total*=nn[j]
            output.append(total)
        return output