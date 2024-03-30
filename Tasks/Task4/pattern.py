# specify the input number
num = 5

for i in range(num*2): # the range is equal to the number of printed lines
    if i <= num:        # increase the number of stars for each line until i reached the input num
        print('*'* i)
    else:               # decrease the number of stars until the end of the for loop.
        print('*'* (2*num-i))