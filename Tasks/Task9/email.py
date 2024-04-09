### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails. 
    has_been_read = False

    # constructor method
    def __init__(self, email_address, subject_line, email_content):
    # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email('joshua@mail.com',
                    'Job Offer!',
                    'Congratulation! After close consideration, we want to offer you the job!')
    email_2 = Email('harry@mail.com',
                    'Hello old Friend',
                    'Hey Harry, it has been a while since we have spoken. How are you doing?')
    email_3 = Email('nicole@mail.com',
                    'Package Delivery',
                    'Hi Nicole, your package will be delivered by our special courier service a 11:00AM tomorrow.')
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)


def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print('')
    for index, email in enumerate(inbox):
        print(index, email.subject_line)
    print('')


def read_email(index):

    # Create a function which displays a selected email. 
    email = inbox[index]
    print(f'\nFrom: {email.email_address}')
    print(f'Subject: {email.subject_line}')
    print(f'Content:\n{email.email_content}')
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email.mark_as_read()
    print(f'\nEmail from {email.email_address} marked as read.\n')


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True
populate_inbox()

while True:

    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # logic to read an email
        list_emails()
        while True:
            try:
                num = int(input(
                    '\nPlease select the number of the email you want to read: '))
                if num < len(inbox):
                    break
                else:
                    print(f'\nOops - incorrect input. Please enter a number in range 0 - {len(inbox)-1}')
                
            except ValueError:
                print('\nOops = invalid input. Please enter a number.')
        
        read_email(num)
        
    elif user_choice == 2:
        # logic to view unread emails
        print('\nUnread emails:\n')
        # initializing list of unread emails
        unread = []
        for email in inbox:
            if email.has_been_read == False:
                unread.append(f'{email.subject_line}\n')
        if len(unread) == 0:
            print('All emails have been read!')
        else:
            print(''.join(unread))
            
    elif user_choice == 3:
        # logic to quit appplication
        print('\nYou have chosen to Quit the application, Goodbye!')
        break

    else:
        print("\nOops - incorrect input.")
