class MinStack:

    def __init__(self):
        # We store elements as tuples: (actual_value, minimum_at_this_point)
        self.stack = [] 

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            # Look at the minimum value of the previous element (-1 fetches the last element, [1] gets its minimum)
            current_min = min(val, self.stack[-1][1])
            
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # [-1] gets the top tuple, [0] extracts the actual value
        return self.stack[-1][0]

    def getMin(self) -> int:
        # [-1] gets the top tuple, [1] extracts the running minimum
        return self.stack[-1][1]
