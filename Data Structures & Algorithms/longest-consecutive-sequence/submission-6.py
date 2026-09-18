class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setVal = set(nums)
        current = 0
        longest = 0

        for i in nums:
            if i-1 not in setVal:
                while (i + current) in setVal:
                    current += 1
                longest = max(current,longest)
                current = 1
        return longest
        

            
        