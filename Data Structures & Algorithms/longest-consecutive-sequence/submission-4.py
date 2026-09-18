class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current = 1
        longest = 1
        if nums == []:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                current += 1
                longest = max(longest,current)
            elif nums[i+1] == nums[i]:
                continue
            else:
                current = 1
        return longest
            
        