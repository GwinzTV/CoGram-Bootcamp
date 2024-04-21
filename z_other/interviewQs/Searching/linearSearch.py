
input = [4,2,5,1,12,9,3,10]

def linearS(list, target):
    for i,x in enumerate(list):
        if x == target:
            return f'{target} is in index position {i} of the list'


def main():
    print(linearS(input, 9))



if __name__ == "__main__":
    main()