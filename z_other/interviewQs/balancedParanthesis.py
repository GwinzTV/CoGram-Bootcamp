'''
Question: Implement a function that checks if a given string of parantheses is
balanced using a stack.
'''


def is_balanced(input):
    stack = []
    for char in input:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def main():
    print(is_balanced("(())"))
    print(is_balanced("(()"))
    print(is_balanced("(())))"))


# test:
if __name__ == "__main__":
    main()
