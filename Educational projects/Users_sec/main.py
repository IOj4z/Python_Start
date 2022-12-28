import csv


def getData():
    file = list(csv.reader(open('passwords.csv')))
    tmp = []
    for i in file:
        tmp.append(i)
    return tmp


def newUser(tmp):
    name_again = True
    while name_again:
        userId = input('Enter new user ID: ').lower()
        exist = False
        row = 0
        for i in tmp:
            if userId in tmp[row][0]:
                print(userId, ' has already been allocated')
                exist = True
            row = row + 1
        if exist == False:
            name_again = False
    return userId


def findUser(tmp):
    userId = ''
    retry = True
    while retry:
        searchId = input('Enter the user ID you are looking for ')
        searchId.lower()
        exist = False
        row = 0
        for i in tmp:
            if searchId in tmp[row][0]:
                exist = True
            row = row + 1
        if exist:
            userId = searchId
            retry = False
        else:
            print(searchId, ' is Not in list!')
    return userId


def createPass():
    sclist = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "?", "@", "#"]
    nclist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    retrys = True
    while retrys:
        score = 0
        uc = False
        lc = False
        sc = False
        nc = False
        password = input('Enter password: ')
        password2 = password
        length = len(password)
        if length >= 8:
            score = score + 1
        for x in password:
            if x.islower():
                lc = True
            if x.isupper():
                uc = True
            if x in nclist:
                nc = True
        if sc == True:
            score = score + 1
        if lc == True:
            score = score + 1
        if uc == True:
            score = score + 1
        if nc == True:
            score = score + 1
        if score == 1 or score == 2:
            print('This pass too weak!')
        if score == 3 or score == 4:
            print('This password could be improved')
            retry = input('Do you want to try to make stronger password? (y/n): ')
            retry.lower()
            if retry == 'n':
                retrys = False
        if password != password2:
            print('Passwords do not match. File not saved')
            main()
        else:
            return password


def changePass(userId, tmp):
    if userId != '':
        password = createPass()
        Id = userId.index(userId)
        tmp[Id][1] = password
        file = open('passwords.csv', 'w')
        x = 0
        for row in tmp:
            newRecord = tmp[x][0] + ', ' + tmp[x][1] + '\n'
            file.write(newRecord)
            x = x + 1
        file.close()


def displayUsers():
    tmp = getData()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x = x + 1


def main():
    list = ['1) Create a new User ID', '2) Change a password', '3) Display all User IDs', '4) Quit']
    tmp = getData()

    while True:
        for i in list:
            print(i)
        userslect = int(input('Enter number: '))
        match userslect:
            case 1:
                userId = newUser(tmp)
                password = createPass()
                file = open('passwords.csv', 'a')
                newRecord = userId + ', ' + password + '\n'

                file.write(str(newRecord))
                file.close()
            case 2:
                userId = findUser(tmp)
                changePass(userId, tmp)
            case 3:
                displayUsers()
            case 4:
                return False
            case _:
                print('Incorrect number')


if __name__ == '__main__':
    main()
