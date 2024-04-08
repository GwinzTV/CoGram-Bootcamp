
class Alternate:
    # == initializing the class == #
    def __init__(self):
        self.result = ''
        # == asks user for input and stores input in global variable == #
        self.user_input = input(
            '''Hi user!, Please enter your sentence:\n''')
    
    # == capitalises the alternating characters of the user input == #
    def characters(self):
        result = []
        string = self.user_input
        for i in range(len(string)):
            if i % 2 == 0:
                result.append(string[i].upper())
            else:
                result.append(string[i].lower())
        self.result = ''.join(result)
        print('')
        print('Alternating characters:')
        print(self.result)
        print('')

    # == capitalises the alternating words of the user input == #
    def words(self):
        result = []
        string = self.user_input.split()
        for i in range(len(string)):
            if i % 2 == 0:
                result.append(string[i].upper())
            else:
                result.append(string[i].lower())
        self.result = ' '.join(result)
        print('')
        print('Alternating words:')
        print(self.result)
        print('')


# Script:
alt = Alternate()
alt.characters()
alt.words()