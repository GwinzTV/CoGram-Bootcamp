'''
This is teh merge sort algorithm!!
'''
import math as m

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = m.floor(len(arr)/2)
    leftArr = arr[0 : middle]
    rightArr = arr[middle : len(arr)]

    return merge(mergeSort(leftArr),  mergeSort(rightArr))

def merge(left, right):
    leftPointer = 0
    rightPointer = 0
    ordered = []

    while leftPointer < len(left) and rightPointer < len(right):
        # if element in left array is greater than element in right array, add left element to the ordered list
        if left[leftPointer] < right[rightPointer]:
            ordered.append(left[leftPointer])
            leftPointer += 1
        # if element in right array is greater than element in left array, add right element to the ordered list
        else:
            ordered.append(right[rightPointer])
            rightPointer += 1
    # return ordered list of elements, where the one of the add ons is an empty list, and the other is the greatest element between the two arrays
    return ordered + left[leftPointer:] + right[rightPointer:]



def main():
    result = mergeSort([5,2,6,15,8,3,9])
    print(result)


if __name__ == "__main__":
    main()