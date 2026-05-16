class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_list=list(s)
        t_list=list(t)
        for char in s_list:
            if char in t_list:
                t_list.remove(char)
            else:
                return False
        if len(t_list) == 0:
            return True
        else:
            return False