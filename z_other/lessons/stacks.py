'''
Common uses of Stacks:
 - Function and Recursive calls
 - Undo and Redo Mechanisms
 - "Most recently used" features
 - Backtracking algorithms
 - Expression evaluations and syntax parsing
'''

class Stack:
    def __init__(self, max):
        self.max_size = max
        self.stack = [None] * max
        self.top = -1

    # push value to the top of the stack
    def push(self, value):
        if self.top == self.max_size - 1:
            print("Error: Stack Overflow!")
            return
        self.top += 1
        self.stack[self.top] = value

    # pop value from the top of the stack
    def pop(self):
        if self.top == -1:
            print("Error: Stack Underflow!")
            return
        removed = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return removed



def main():
    stack = Stack(5)
    print(stack.stack)
    for i in range(0,10,2):
        stack.push(i)
        print(stack.stack)
    
    for i in range(5):
        stack.pop()
        print(stack.stack)



if __name__ == "__main__":
    main()