'''
This script modifies the merge sort algorithm to order a list of
strings by string length from the longest to the shortest.
'''
sample1 = ['Dog', 
           'Elephant',
           'Pizza',
           'Computer',
           'Banana',
           'Supernova',
           'Moon',
           'Mountain',
           'Butterfly',
           'Galaxy']

sample2 = ['Apple',
           'Carrot',
           'Penguin',
           'Television',
           'Ocean',
           'Laptop',
           'Dragonfly',
           'Sunflower',
           'Elephant',
           'Mountain']

sample3 = ['Book',
           'Rainbow',
           'Helicopter',
           'Giraffe',
           'cat',
           'Waterfall',
           'Butterfly',
           'Elephant',
           'Universe',
           'Volcano']


# merge sort an array of integer lengths of the words
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    left = arr[0 : middle]
    right = arr[middle : len(arr)]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    leftPointer = 0
    rightPointer = 0
    while leftPointer < len(left) and rightPointer < len(right):
        # here I modified the merge sort to compare the length of 
        # the elements instead of their value
        if len(left[leftPointer]) > len(right[rightPointer]):
            result.append(left[leftPointer])
            leftPointer += 1
        else:
            result.append(right[rightPointer])
            rightPointer += 1
    
    return result + left[leftPointer:] + right[rightPointer:]


def main():
    print(mergeSort(sample1))
    print(mergeSort(sample2))
    print(mergeSort(sample3))



if __name__ == "__main__":
    main()