'''
In this script I have created a function that takes in an array 'arr' and recursively
finds and outputs the largest number in the list.

Thanks for reviewing my submission, I value your feedback!!!
'''

def validate_input(array):
     # if array is anything else but integers raise value error
    if not all(isinstance(x, int) for x in array):
        raise ValueError("Array must contain integer values only!")

# recursive function definition
def largest(arr: list[int]):
    try:
        validate_input(arr)
    except ValueError as e:
        print("Error:", e)
    else:
        # base case: if there is only one number left in array, return it because it is the largest number.
        if len(arr) == 1:
            return arr[0]
        # logic to remove smallest value from array during each recursive call.
        smallest = min(arr)
        arr.remove(smallest)
        # recursive call
        return largest(arr)

# main function to test functionality
def main():
    result = largest([1,6,12,7,18,9,2])
    print(result)


# run below block of code if the script is not being imported as a module
if __name__ == "__main__":
    main()