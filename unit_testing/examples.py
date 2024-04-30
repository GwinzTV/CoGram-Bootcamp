def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total


def get_first_sorted_name(names):
    names.sort()
    name = names[1]
    return name


def get_middle_value(num_list):
    middle = len(num_list)//2
    return num_list[middle]

