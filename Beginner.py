

users = {}  
status = "" 


def displaymenu():  
    status = input('are you a registerd user?')
    if status == 'y':
        oldUser()
    elif status == 'n':
        newUser()


def newUser():
    createlogin = input('create your codex')

    if createlogin in users:
        print('login already exists')
    else:
        createpassw = input('create password')
        users[createlogin] = createpassw
        print('User created')


def oldUser():
    login = input('Enter login name')
    passw = input('Enter the password')

    if login in users and users[login] == passw:
        print('login successful')
    else:
        print('user does not exist or wrong password')


while status != 'q':
    displaymenu()

