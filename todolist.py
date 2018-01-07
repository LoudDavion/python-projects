import sys




def add(file, item):
    file.write(item[4:] + '\n')
    file.seek(0)
    print(file.read())

def rm(file, n):
    if not (file.read())[3:]:
        print('Nothing to do!')
        


with open('usertodo.txt', 'w+') as a:
    userlist = a
    if not userlist.read():
        userlist.write("To Do List: \n")
        userlist.seek(0)
    print(userlist.read())
    
    quitter = False
    while (quitter == False):
        userin = input("Enter a command(add, rm, quit, print: ")
        if userin[:3] == 'add':
            add(userlist, userin)
        if userin[:2] == 'rm':
            rm(userlist, 3)



