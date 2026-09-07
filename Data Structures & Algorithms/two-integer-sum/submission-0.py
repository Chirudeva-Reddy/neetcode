class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        list_ = []
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    list_.append(i)
                    list_.append(j)
                    
                    return list_