class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index , a in enumerate(nums):
            #condition to eliminate duplicates
            if index > 0 and a == nums[index-1]:
                continue 
            l,r = index + 1, len(nums)-1
            while l < r:
                threeSum =  a + nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    #final condition for updating either the left/right pointer
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res