import random
import time

# n = random.randrange(0, 9999999999)
# n = [n]


database = {}


def init():
    isValidOptionSelected = False
    print('welcome to Reel Bank')

    while isValidOptionSelected == False:
        try:
            haveAccount = int(input('have account: 1 (yes) 2(no) \n'))

            if haveAccount == 1:
                isValidOptionSelected = True
                login()
            elif haveAccount == 2:
                isValidOptionSelected = True
                print(register())
            else:
                print('invalid option')
        except ValueError:
            print('wrong value')



def login():
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        try:
            accountNumberFromUser = int(input('Your account number'))
            passwordFromUser = input('your password')
            for accountNumber, password, email in database.items():
                if accountNumber == accountNumberFromUser:
                    isLoginSuccessful = True
                else:
                    print('invalid')
                    if password == passwordFromUser:
                        isLoginSuccessful = True
                    else:
                        print('invalid')
        except ValueError:
            print('try again')
    #bankOperation()


def register():
    global firstName, lastName, gmail
    email = False
    print('fill in details')
    time.sleep(1)
    while not email:
        gmail = input('enter email \n')
        if gmail.endswith('@gmail.com'):
            firstName = input("enter firstname \n")
            lastName = input("enter lastname \n")
            break
        else:
            print('Email must be in this format ' + 'example123@gmail.com')

    check = False
    while not check:
        password = input("create password \n")
        confirmpassword = (input('confirm password \n'))
        if password == confirmpassword:
            accountNumber = generateUserAccountNumber()
            print('Hello', firstName, 'This are your details, not '
                                      'correct press 1 to make corrections')
            database[accountNumber] = {
                'first name': firstName,
                'last name': lastName,
                'email': gmail,
                'password': password,
                'account number': accountNumber
            }
            print('account created')
            print('account number is %s' % accountNumber)
            print('account password is %s' % password)
            time.sleep(3)
            _login = input('Do you want login? 1 == yes \n 2 == no \n')
            if int(_login) == 1:
                login()
            else:
                bankOperation()

        else:
            print("password don't match")


def bankOperation():
    print('bank operations')


def generateUserAccountNumber():
    time.sleep(2)
    return random.randrange(1111111111, 9999999999)


##system##

init()

generateUserAccountNumber()
