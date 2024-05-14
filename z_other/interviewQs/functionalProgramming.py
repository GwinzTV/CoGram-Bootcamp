'''
Question: Implement a function called apply_operation that takes a function as an argument and returns
          a new function that applies the given function to its argument and doubles the result.
'''


def apply_operation(func):
    def newfunc(arg):
        return 2 * func(arg)
    return newfunc


def square(a):
    return a * a


def main():
    double_square = apply_operation(square)
    result = double_square(2)
    print(result)


if __name__ == "__main__":
    main()
