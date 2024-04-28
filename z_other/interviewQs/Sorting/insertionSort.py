'''

'''

input = [12,11,13,5,6,1,-1]

def insertionS(arr):
    # iterate through list starting from second element
    for i in range(1, len(arr)):
        # set a variable to access the (i-1)th element
        j = i - 1
        # define the ith element
        value = arr[i]
        # compare each ith element to the rest of the elements on the left and sort
        while j >= 0 and value < arr[j]:
            # if current ith element is smaller than arr[j] swap the elements
            arr[j + 1] = arr[j]
            j -= 1
            # loop breaks when the j pointer reaches the left end of the list
        # assign value to its correct position
        arr[j + 1] = value

def main():
    insertionS(input)
    print(input)


if __name__ == "__main__":
    main()