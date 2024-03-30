# take in the times of each event and store them in a list
# calculate the sum of all the times
# if the sum of times is between 0 and 100 minutes then print Provincial colours
# else if the time is within 5 minutes of qualifying time then print Provincial half colours
# else if the time is within 5 minutes of qualifying time print Provincial scroll
# else if the time is more than 10 minutes off from the qualifying time print No award

time = []

time.append(int(input('Enter your time for the Swinmming: ')))
time.append(int(input('Enter your time for the Cycling: ')))
time.append(int(input('Enter your time for the Running: ')))

total_time = sum(time)

if 0<=total_time<=100:
    print('You are awarded: Provincial colours')
elif 101<=total_time<=105:
    print('You are awarded: Provincial half colours')
elif 106<=total_time<=110:
    print('You are awarded: Provincial scroll')
else:
    print('You are awarded: No award')