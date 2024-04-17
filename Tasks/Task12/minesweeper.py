'''
This script takes a sample minefield of "-"'s and "#"'s, where each "#" is 
a mine and each "-" is a mine-free spot, and returns a new minefield with
each dash replaced by a digit, indicating the number of mines immediately,
adjacent to the spot i.e. horizontally, vertically, and diagonally.
'''

# sample input minefield
minefield = [["-", "-", "-", "#", "#"],
             ["-", "#", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "#", "#", "-", "-"],
             ["-", "-", "-", "-", "-"]]

# method to check for mine around specific element in grid
def check_surroundings(row, col, number_row, number_col):
    # list of all the coordinates around the current element in the grid
    coordinates = [[row-1,col-1], [row-1,col], [row-1,col+1],
                   [row,col-1], [row,col], [row,col+1],
                   [row+1,col-1], [row+1,col], [row+1,col+1]]
    counter = 0
    # checks if mine is in current position
    if minefield[row][col] == "#":
        return "#"
    # iterates through coordinates and logs how many mines are present
    else:
        for r,c in coordinates:
            # this conditional makes sure that we are looking for elements that are not out of bounds of the lists in the 2D array
            if 0<=r<number_row and 0<=c<number_col:
                # if there is a mine at the coordinate add to the counter
                if minefield[r][c] == "#":
                    counter += 1
        # return number of mines found around the current coordinate as a string
        return str(counter)
    

# main function
def main():
    # defining the dimensions of the 2D array
    number_of_col = len(minefield[0])
    number_of_row = len(minefield)
    # initialise an empty minefield of the same dimensions
    new_minefield = [[None] * number_of_col for _ in range(number_of_row)]
    # submitting index values of each element to the function, then populating the result of the function to the new 2D array
    for r, row in enumerate(minefield):
        for c, _ in enumerate(row):
           new_minefield[r][c] = check_surroundings(r, c, number_of_row, number_of_col)
    # display the new minefield
    for i in new_minefield:
        print(i)

    # # uncomment the below for loop, and comment the above for loop for a more visually pleasing representation of what the script just did!
    # for i in range(number_of_row):
    #     if i == number_of_row//2:
    #         print(minefield[i], end='')
    #         print(' ===>  ', end='')
    #         print(new_minefield[i])
    #     else:
    #         print(minefield[i], end='\t')
    #         print(new_minefield[i])
    

# run below block of code if the script is not being imported as a module
if __name__ == '__main__':
    main()

'''
****************************
** Note for Code Reviewer **
****************************

I had a lot of fun solving this program, using the hint given in the document,
I was able to quickly solve this task first time, without testing, because now I have started
thinking computationally. In my spare time I added some extra print formatting just to 
present before and after of the unsolved and solved minefield (just for fun!).

Thanks for reviewing my code, I value all your feedback!!!
'''