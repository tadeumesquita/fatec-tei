import collections
from random import choice

def createUser(name,users):
    user = name[0].lower() + name.split(" ")[-1].lower()
    
    for u in users:
        if user == u.user:
            user += choice('123456789')

    return user
    
def createPasswd(size):
    passwd = ''
    while size > 0:
        passwd += choice('0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM!@#$%¨&*()_+-=')
        size = size - 1
    return  passwd

def main():          
    User = collections.namedtuple("User","name user passwd")
    
    users = []
      
    control = 1

    print("==CADASTRO DE USUÁRIOS==")
    while control != 'q':
        control = input("Digite o nome do usuario ou q para sair: ")
        if control != 'q':
            users.append(User(control,createUser(control,users),createPasswd(8)))

    print("Nome  Usuario  Senha")

    users.sort()

    for u in users:
        print(u.name, end=" ")
        print(u.user, end=" ")
        print(u.passwd)

main()