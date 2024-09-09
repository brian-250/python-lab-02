# Name: Brian Milian
# Date: 9/9/24
# File Purpose: Tuffy Titan's Contacts List Manipulation

contacts = []

def print_list(contacts):
    """
    Prints each list in 'contacts' on a new line.

    Paramters:
    contacts (2D list): The only list in the parameter.

    Methods:
    print():
        Prints a title for Tuffy Titan's 'contacts' list.
    print():
        Prints a header for the index number, first name, and last name of
        each list in 'contacts'.
    print():
        Prints each list in 'contacts' in the chronilogical format
        of: index number, first name, and last name.
    """
    print("------------TUFFY TITAN'S CONTACTS LIST-------------")
    print("#-------First Name------------Last Name-------------")
    for i in contacts:
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
