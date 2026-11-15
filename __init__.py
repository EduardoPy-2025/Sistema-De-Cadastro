from lib import *   
from colorama import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True   
      
def Cadastrar(arq, nome, idade, plano):
    planos = ("premium", "kids", "vip", "básico")

    if plano not in planos:
        print("Erro! Selecione um plano válido.")
        return False

    try:
        with open(arq, "at", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{idade};{plano}\n")

        print(f"O usuário {nome} foi cadastrado.")
        return True

    except OSError as erro:
        print(f"Erro ao salvar o cadastro: {erro}")
        return False


def LerArquivo(nome):
    try:
        with open(nome,"rt", encoding="utf-8") as ar:
            cabeçalho('PESSOAS CADASTRADAS')
            
            for linha in ar:
              if not linha.strip():
               continue
        
              dado = linha.strip().split(';')
              if len(dado) != 3:
               continue
           
              print(
               f'{dado[0]:<17}'
               f'{dado[1]:>5}anos    '     
               f'Plano / assinatura: {dado[2]}'
             )
    except FileNotFoundError:
        print("Error! o arquivo não foi criado.")
        
    except OSError as error:
        print(f"Não foi possível ler o arquivo: {error}")      
         
def CriarAquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Error! Arquivo não foi criado! :(")
    else:
        print(f"O Arquivo {nome} foi criado com sucesso! ")        
    