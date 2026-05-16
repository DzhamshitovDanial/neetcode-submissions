class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        mx=0
        count={}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            if (right-left+1)-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            mx=max(mx,right-left+1)
        return mx