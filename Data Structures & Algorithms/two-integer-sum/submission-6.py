class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        prevMap = {}  # val:index
        for index,val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff],index]
            else:
                prevMap[val] = index

