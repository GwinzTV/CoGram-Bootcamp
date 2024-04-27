'''
Linear search
'''

def linear_search(arr, target):
    for i in arr:
        if i == target:
            return f'{target} found at index {i}'
    return f'{target} not in the list'


'''
Binary search
'''

def binary_search(arr, target):
    low = 0
    high = len(arr)
    def recursion(low, high):
        mid = (low + high)//2

        if low > high:
            return f'{target} not in the list'
        if arr[mid] == target:
            return f'{target} found at index {mid}'
        if arr[mid] < target:
            return recursion(mid+1, high)
        else:
            return recursion(low, mid-1)
    return recursion(low, high)


def main():
    array = [4,1,7,12,9,6]
    target = 9

    linear = linear_search(array, target)
    binary = binary_search(sorted(array), target)

    print(f"Linear: {linear}")
    print(f"Binary: {binary}")



if __name__ == "__main__":
    main()