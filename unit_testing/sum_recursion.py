'''
In this script I have created a function that takes in two arguments, an array 'arr' and an integer 'n'.
the function recursively adds all the elements in the list up to and including the nth value in the array.

Thanks for reviewing my submission, I value your feedback!!!
'''

def validate_input(array):
     # if array is anything else but integers raise value error
    if not all(isinstance(x, int) for x in array):
        raise ValueError("Array must contain integer values only!")

# recursive function definition
def sum_array(arr, n):
    try:
        validate_input(arr)
    except ValueError as e:
        print("Error:", e)
    else:
        # base case, which returns the first element in the arr
        if n == 0:
            return arr[0]
        # recursive call that adds the nth array element with the (n-1)th element in the array, where n is the index position
        return arr[n] + sum_array(arr, n-1)
    
# main function to test functionality
def main():
    result = sum_array([1,2,3,4,5,6,7,8,9,10],6)
    print(result)


# run below block of code if the script is not being imported as a module
if __name__ == "__main__":
    main()