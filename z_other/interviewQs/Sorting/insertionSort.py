'''

'''

input = [12,11,13,5,6,1,-1]

def insertionS(arr):
    for i in range(1, len(arr)):
        j = i - 1
        value = arr[i]
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

def main():
    insertionS(input)
    print(input)


if __name__ == "__main__":
    main()