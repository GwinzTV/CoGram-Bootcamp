'''
example fiibonacci code using recursion:
'''

def fibonacci(n):
    # base case is either 1 or 0 
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

# print(fibonacci(6))

'''
example binary search using recursion:
funny enough i just figured out that nested function are a thing :)
I will definitely be using them where neccesary  going forward
'''

def binary_prac(arr,target):
    def recursion(low, high):
        # base case, if target not in array
        if low > high:
            return f'{target} not in array!'
        
        # calculate mid
        mid = (low + high) // 2

        # check if mid is target
        if arr[mid] == target:
            return f'{target} is at index {mid}'
        
        # search left side if target is less than mid
        if target < arr[mid]:
            return recursion(low, mid - 1)
        
        # search right side if target is more than mid
        if target > arr[mid]:
            return recursion(mid + 1, high)
        
    return recursion(0, len(arr) - 1)


print(binary_prac([1,2,3,4,5,6,7,8,9],3))
print(binary_prac([1,2,3,4,5,6,7,8,9],5))
print(binary_prac([1,2,3,4,5,6,7,8,9],7))
print(binary_prac([1,2,3,4,5,6,7,8,9],8))
print(binary_prac([1,2,3,4,5,6,7,8,9],2))
print(binary_prac([1,2,3,4,5,6,7,8,9],12))


def factorial(value):
    if value == 0:
        return 1
    result = value * factorial(value - 1)
    return result

n = 5
print(f'\nfactorial of {n}')
print(factorial(n))