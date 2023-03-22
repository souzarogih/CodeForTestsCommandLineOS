import os
import requests
import json


# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)


# diretorio atual do programa
cwd = os.getcwd()
print(cwd)
# '/home/dinsdale'

file = os.path.abspath('memo.txt')
# '/home/dinsdale/memo.txt'
print(file)

print("list: ", os.listdir(cwd))
print(type(os.listdir(cwd)))
# ['music', 'photos', 'memo.txt']

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print("->", path, "|", type(path))
        else:
            walk(path)

walk("C:\\Users\\higor.souza\\PycharmProjects\\firstCodeFastApi")

# pega o usuário da maquina
print(os.getlogin())


print(os.getpid())
print(os.getlogin())
# print(os.uname())

statinfo = os.stat('somefile.txt')
print(statinfo)


# pegando o nome do arquivo
path = "C:\\Users\\higor.souza\\PycharmProjects\\firstCodeFastApi\\somefile.txt"
print(path)
tst = path.split('\\')
print(type(tst))
print(tst[-1])
print(type(tst[-1]))
tt = tst[-1]
#print()

def pesq():
    raw_file_content = """Hi there and welcome. This is a special hidden file with a SECRET secret. I don't want to tell you The Secret, but I do want to secretly tell you that I have one."""

    if "welcome" in raw_file_content:
        print("exite")
    else:
        print("Não existe")

pesq()



ree = requests.get('https://www.paystore.com.br/')
print(ree)
print(ree.status_code)



# https://pense-python.caravela.club/14-arquivos/04-nomes-de-arquivo-e-caminhos.html
# https://realpython.com/python-string-contains-substring/
# https://realpython.com/python-string-contains-substring/
# https://github.com/caiorodro/Logging_Microservice