'''
The bubble sort will sort compare each item in the list with its neighbours to see if it is larger and if so it will
move this item higher in the list until its can't
'''

sample_list = [12,4,2,5,1,9,3,8]

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
            


def main():
    result = bubble_sort(sample_list)
    print(result)


if __name__ == "__main__":
    main()