class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        mul_L = 1
        for i in range(n):
            output[i] = mul_L
            mul_L *= nums[i]
            
        mul_R = 1
        for i in range(n - 1, -1, -1):
            output[i] *= mul_R
            mul_R *= nums[i]
            
        return output