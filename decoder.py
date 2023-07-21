def printMenu():
    print("Menu")
    print('-------------')
    print("1. Encode")
    print('2. Decode')
    print('3. Quit')

def main():
    menuInput = ''
    userPass = ''
    end = 0
    while end == 0:
        printMenu()
        menuInput = input("Please enter an option: ")

        if menuInput == '1':
            userPass = passEncode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')

        if menuInput == '2':
            print(f'The encoded password is {userPass}, and the original password is {passDecode(userPass)}.')
        
        if menuInput == '3':
            end = 1

            
def passEncode(userPass):
    encPass = ''
    for char in userPass:
        encPass = encPass + str(int(char) + 3)
    return encPass

def passDecode(userPass):
    decPass = ''
    for char in userPass:
        decPass =  decPass + str(int(char) - 3)
    return decPass


        
main()