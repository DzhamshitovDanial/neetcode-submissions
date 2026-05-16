class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maximum=0
        i=0
        while left<right:
            n=min(height[left],height[right])*(right-left)
            if n>maximum:
                    maximum=n
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
            i+=1
        return maximum
