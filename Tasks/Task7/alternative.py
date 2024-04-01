
class alternate:
    def __init__(self):
        self.result = ''
        self.user_input = input("Hi user!, Please enter your sentence:\n")
    
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
alt = alternate()
alt.characters()
alt.words()