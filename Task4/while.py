# continuosly prompt the user for a number:
num = 0
num_list =[]
while num != -1:
    num = int(input('Please enter a number: '))
    # if the input number is -1 then stop prompting user for input:
    if num == -1:
        break
    elif num != 0:
        num_list.append(num)

# calculate the average of all the numbers entered:
print(sum(num_list)/len(num_list))