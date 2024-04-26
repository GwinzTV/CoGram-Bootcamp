'''
This is QuickSort, one of the most efficient ways to sort a list!
'''

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    # removes the last element in the list
    pivot = arr.pop()
    # arrays to collects elements less than and greater than current pivot
    lesser = []
    greater = []

    # arranging the elements into lesser or greater arrays
    for x in arr:
        if x <= pivot:
            lesser.append(x)
        else:
            greater.append(x)
    # recursive call
    return quickSort(lesser) + [pivot] + quickSort(greater)


def main():
    result = quickSort([5,2,8,12,6,9,1])
    print(result)


if __name__ == '__main__':
    main()