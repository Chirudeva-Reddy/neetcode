class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        curr_area = 0
        i,j =0 , len(heights)-1
        while i < j:
            curr_area = min(heights[i],heights[j])*(j-i)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] >= heights[i]:
                i += 1
                
            if curr_area > max_area:
                max_area = curr_area
        return max_area