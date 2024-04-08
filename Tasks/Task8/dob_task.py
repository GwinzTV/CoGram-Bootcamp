
with open('DOB.txt', 'r') as file:
    # read in each line in the file as a list item
    lines = file.readlines()
    # initialise the two lists that will store the sorted input information
    names = []
    dobs = []
    # split and sort the name and DOB into their respective lists
    for line in lines:
        line = line.replace('\n', '').split()
        names.append(line[0:2])
        dobs.append(line[2:])

    # == iterate though list of names and print them out == #
    print('\n# == Name == #\n')
    for name in names:
        print(' '.join(name))
    
    # == iterate though list of DOBs and print them out == #
    print('\n# == Birthdate == #\n')
    for dob in dobs:
        print(' '.join(dob))


