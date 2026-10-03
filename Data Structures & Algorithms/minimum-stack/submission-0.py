class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

        #if min_stack is empty,append with element
        if not self.min_stack:
            self.min_stack.append(val)
        #otherwise, set current_min to a comparision b/w TOS(min stack) and incoming element
        else:
            current_min = min(val,self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #will return the top of min_stack(will always be the min_element cuz we are appending it that way)
        return self.min_stack[-1]
