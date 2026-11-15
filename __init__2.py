from colorama import init, Fore, Style
init(autoreset=True)
from time import sleep

def validarNome(nome):
    for letra in nome:
        if letra.isdigit():
            return False
    return True    

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError, TypeError:
            print(Fore.RED+"ERROR! Tivemos um problema com o tipo de dado :(")    
        except SyntaxError:
            print("Error Syntax")    
        except Exception as error:
            print(Fore.RED+f"Error! Por favor, digite um numero válido. {error.__class__}")    
        except KeyboardInterrupt :
            print(Fore.YELLOW + "O usuário preferiu não seguir com a operação! Encerrando o progama...")   
            return None
        else:
            return n    

def linha(tam=43):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(43)) 
    print(linha())


def menu(lista):
     cabeçalho(Fore.MAGENTA+"MENU PRINCIPAL".center(43))
     c=1
     for item in lista:
        print(f'{c} - {item}')
        c += 1
     print(linha())
     opc = LeiaInt(Fore.GREEN+"Sua opção: ")
     return opc
