# ask the user to enter a sentence and save the users response:

str_manip = input('Enter a senstence: ')

# calculate and print out the length of the input string:

print(len(str_manip))

# find the last letter in the variable str_manip,
# and replace every occurence of this letter in str_manip with '@':

str_manip1 = str_manip.replace(str_manip[-1], '@')
print(str_manip1)

# print the last characters of str_manip backwards:

print(str_manip[-1:-4:-1])

# create a five-letter word that is made up of the first three characters and the last two characters in str_manip:

five_letter_word = str_manip[0:3] + str_manip[-2:]
print(five_letter_word)