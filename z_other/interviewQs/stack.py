'''
Question: Implement a stack using a python list. Include push, pop, and is_empty methods.
'''

class Stack:
    # initialise a stack array
    def __init__(self):
        self.stack = []
        self.top = -1

    # push method complexity: O(1)
    def push(self, value):
        self.stack.append(value)
        self.top += 1

    # pop method
    def pop(self):
        if self.is_empty():
            print("Error: Stack Underflow!")
            return
        self.top -= 1
        return self.stack.pop()
    
    def is_empty(self):
        return self.top == -1
    
# test:
def main():
    stack = Stack()
    for i in range(0,10,2):
        stack.push(i)
        print(stack.stack)
    for i in range(0,10,2):
        stack.pop()
        print(stack.stack)


if __name__ == "__main__":
    main()