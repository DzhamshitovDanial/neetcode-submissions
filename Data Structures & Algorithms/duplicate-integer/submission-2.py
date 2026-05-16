class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
          s=[]
          for i in range(len(nums)):
                 if not nums[i] in s:
                     s.append(nums[i])
          if len(s)==len(nums):
              return False
          else:
              return True