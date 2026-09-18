class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setVal = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in setVal:
                current =1
                while (i + current) in setVal:
                    current += 1
                longest = max(current,longest)
        return longest
        

            
        