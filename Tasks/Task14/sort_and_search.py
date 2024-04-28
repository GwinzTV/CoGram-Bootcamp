'''
searching and sorting combined, and thought process
'''

sample_arr = [27,-3,4,5,35,2,1,-40,7,18,9,-1,16,100]

'''
Which searching algorithm would be appropriate to use on the given list?

Seeming as though we have a relatively short unsorted array, I would opt to use linear search for this array
as opposed to binary search. I believe this will be quicker than sorting the array and then using binary search.
'''

# implementing linear search
target = 9
for i in sample_arr:
    if i == target:
        print(f'{target} is found at index {i}')
# the above algorithm was a good choice because it is simple to implement and the sample
# array is relatively small. Also there was no specific requirements for time or space 
# complexity, therefore linear search was the appropriate choice.

'''
Insertion sort on the sample array:
'''

def insertionS(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    pass


sam = sample_arr
insertionS(sam)
print(sam)

'''
I choose to use the binary search algorithm to find the target because the array is now sorted.
'''

def binaryS(arr, target):
    def recursion(low, high):
        mid = (low + high) // 2
        if low > high:
            return f'{target} not in input array'
        if arr[mid] == target:
            return f'{target} found at index {mid}'
        if target < arr[mid]:
            return recursion(low, mid - 1)
        else:
            return recursion(mid + 1, high)
        
    return recursion(0, len(arr))

result = binaryS(sam, target)
print(result)

# I would use the binary search algorithm in real life to quickly search and locate records from a database.