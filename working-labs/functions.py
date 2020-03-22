#def hello():
#    print("Hello, World!")
#
#hello()

# https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3

""" # Define function names()
def names():
    # Set up name variable with input
    name = str(input('Enter your name: '))
    # Check whether name has a vowel
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')

    # Iterate over name
    for letter in name:
        print(letter) 

# Call the function
names() """


# Functions with parameters
def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

add_numbers(1, 2, 3)