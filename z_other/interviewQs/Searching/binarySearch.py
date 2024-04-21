
input = [2,3,4,5,6,7,8,9,10,11,12]

def binaryS(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        if list[mid] == target:
            return f'{target} found at position {mid} of the list'
        # check if target is on right hand side and adjust
        elif list[mid] < target:
            low = mid + 1
        # check if target is on left hand side and adjust
        else:
            high = mid - 1

    return f'{target} not found in the list'
        


# return f'{target} is in index position {i} of the list'


def main():
    print(binaryS(input, 10))



if __name__ == "__main__":
    main()