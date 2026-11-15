from colorama import *
from lib import *
from lib.menuarq import *
from time import sleep
from pathlib import Path


cabeçalho('SISTEMA CADASTRO'.center(43))

pasta = Path(__file__).parent
arq = pasta / 'lib' / 'Dados_cadastrados'

if not arquivoExiste(arq):
    CriarAquivo(arq)
  
while True:
     resposta = menu([
    Fore.CYAN + 'Ver Pessoas cadastradas' + Style.RESET_ALL,
    Fore.CYAN + 'Novo cadastro' + Style.RESET_ALL,
    Fore.CYAN + 'Sair do sistema' + Style.RESET_ALL
])
     if resposta == None:
          break
     if resposta == 1:
          cabeçalho("PESSOAS CADASTRADAS")
          LerArquivo(arq)
          
     elif resposta == 2:
          cabeçalho("NOVO CADASTRO")
          while True:
              try:
                 tem_numero = False
                 
                 nome = str(input("Seu nome: ")).strip()
                 if nome == '':
                    print('Inválido! O campo não foi preenchido\n') 
                    print('\n')
                    continue
                 
                 if len(nome) < 3:
                     print("Error! o nome precisa ter no máximo 3 caracteres!\n ") 
                     continue 
                              
                 elif not nome.replace(" ", "").isalpha():
                     print("Digite apenas letras e espaços\n")     
                     continue      
                  
                 else:
                     print("nome aceito! :)")   
                     print("|")
                     
                 for numero in nome:
                     
                    if numero.isdigit():
                       tem_numero = True
                               
                    if tem_numero:    
                      print("Erro! O espaço não foi preenchido! Tente novamente\n")
                      continue
                    break
                                             
              except Exception as error:
                    print("Tivemos um problema! Tente novamente")   
                
              while True:
                  try:
                     idade = int(input("Sua idade: "))

                     if idade < 0:
                       print("Erro! A idade não pode ser negativa.\n")
                       continue

                     if idade < 12:
                        plano = "kids"
                        print("Plano Kids selecionado automaticamente!\n")
                        break    
    
                  except ValueError:
                     print("Erro! Digite uma idade válida.\n")

                 
              if Cadastrar(arq, nome, idade, plano):
                    print("Cadastro concluído!")

                    opcao = input("Deseja continuar? [1/S, 2/N]: ").strip()

                    if opcao == "1":
                        continue
                    elif opcao == "2":
                        print("Saindo... Até logo!")
                        break
                    else:
                        print("Erro! Digite uma opção válida.")
              else:
                print("Não foi possível concluir o cadastro.")
                               
     if resposta == 3:
       cabeçalho(Fore.YELLOW+"Saindo do sistema... Até logo! :)")
       break   
     else:
      print(Fore.RED+"Ops! Digite uma opção válida.")
     


