class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [] #pair : [temp,index]
        offset = 1
        for index,ele in enumerate(temperatures):
            while stack and ele > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (index - stackInd)
            stack.append([ele,index])
        return result












        