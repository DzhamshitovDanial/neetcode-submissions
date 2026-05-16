class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        mx=0
        set_list=set()
        for right in range(len(s)):
            while s[right] in set_list:
                set_list.remove(s[left])
                left+=1
            set_list.add(s[right])
            mx=max(mx,right-left+1)
        return mx