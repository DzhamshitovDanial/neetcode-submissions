class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        
        longest = 1
        current = 1
        
        for i in range(1, len(nums)):
            # Если числа не равны (игнорируем дубликаты)
            if nums[i] != nums[i-1]:
                # Если идут по порядку
                if nums[i] == nums[i-1] + 1:
                    current += 1
                else:
                    # Если цепочка прервалась, обновляем рекорд и сбрасываем счетчик
                    longest = max(longest, current)
                    current = 1
                    
        return max(longest, current)