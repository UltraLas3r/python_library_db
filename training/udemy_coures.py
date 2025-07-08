def some_string_outputs():
    username = 'Miguel Sanchez'
    password = 'secret'

    print(len(username))

    print(f"Your name is {username} and your password is {password}")


def indexing_strings():
    string_one = 'hello I am dog'
    print(string_one[0:5])  #prints out hello from string_one
    print(string_one[::-1])  # print the string in reverse, 1 at a time, this is the "stepover" syntax

    quote = 'to be or not to be'
    print(quote.upper())
    print(quote.replace('be', 'bobberguy'))

    print(quote)


#indexing_strings()

def account_info_program():
    user_name = input("What is ur name: ")
    user_age = int(input("what is ur age: "))
    relationship_status = int(input("Choose single, not single, its complicated (1,2,3): "))

    if relationship_status == 1:
        print(f'Hello, {user_name}, you are {user_age}, and you are SINGLE')

    if relationship_status == 2:
        print(f'Hello, {user_name}, you are {user_age}, and you are NOT SINGLE')

    if relationship_status == 3:
        print(f'Hello, {user_name}, you are {user_age}, and you are COMPLICATED')

    else:
        print("choose a valid option between 1, 2, 3")


#account_info_program()


def what_year_were_you_born():
    birth_year = input('What year were you born?: ')

    age = 2025 - int(birth_year)

    print(f"You are {age} years old")


#what_year_were_you_born()


def password_checker():
    name = input('What is name: ')
    password_v = input('Enter password: ')

    password_len = len(password_v)

    encrypted_pass = '*' * password_len

    print(f'hello, {name}, your password is {encrypted_pass}'.format(name, encrypted_pass))


password_checker()
