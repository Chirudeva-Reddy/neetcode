class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            count[nums[i]] += 1
        
        for i in nums:
            if count[i] > 1:
                return True
            else:
                pass
        return False
