from funcoes.sendemail import email
from funcoes.searchgoogle import google
from funcoes.randompass import randompass
from funcoes.discoverynet import NetworkScanner
from funcoes.temperatura import timetemperatura
from funcoes.calculadora import calc
from funcoes.dolar import conversaodolar
from funcoes.cep import cepsearch
from configuracoes.configs import color, limpar


import time

#------------------------------------------------------------
#------------------Menu
items_menu = {
    "S ou Sair": "Sair",
    "1": "Envio de e-mail",
    "2": "Pesquisa no google",
    "3": "Gerar uma senha aleatória",
    "4": "Quem esta conectado na minha rede",
    "5": "Temperatura",
    "6": "Calculadora",
    "7": "Ver cotação do dolar",
    "8": "Busca de CEP",
}

tamanho = len(items_menu)
loop = 1
choice = 0
while loop == 1:
    print(color.YELLOW + "\nMenu de ferramentas!\n\
                        Created by: Drew.\
                        \n=========================================\n" + color.END)
    for names, values in items_menu.items():
        print(names, " -> ", values)
    choice = input(color.BOLD + "\nQual operação deseja realizar? " + color.END)
    choice = choice

    #------------------------------------------------------------
    #----------------Envio de e-mail
    if choice == '1':
        limpar()
        email()
        
    #----------------Pesquisa no google
    elif choice == '2':
        limpar()
        google()

    #----------------Gerador de senha
    elif choice == '3':
        limpar()
        randompass()    

    #----------------Dispositivos conectados na rede
    elif choice == '4':
        limpar()
        print(color.CYAN + "Verificar dispositivos conectados na sua rede!\n" + color.END)
        NetworkScanner()

        def main():
            ip_inicial = input("Digite o IP inicial (completo): ")
            ip_final = input("Digite o IP final (apenas o último octeto. Ex: 254): ")
            
            
            scan = NetworkScanner()
            scan.scannear_rede(ip_inicial, ip_final)
            
            while(len(scan.threads)>0):
                time.sleep(0.5)
                #print("\n\n*****************\nTHREADS EXISTENTES >> %s\n*****************\n" % len(scan.threads))
            
            scan.ips_online.sort()
            for pc in scan.ips_online:
                print("PC ONLINE >> IP=%s - MAC=%s" % (pc[0], pc[1]))

            print("\nExistem %s dispositivos online neste momento\n\n" % len(scan.ips_online))
            
            return 0

        if __name__ == '__main__':
            main()
        
    #----------------Temperatura
    elif choice == '5':
        limpar()
        timetemperatura()

    #----------------Calculadora
    elif choice == '6':
        limpar()
        calc()

    #----------------Cotação do dolár
    elif choice == '7':
        limpar()
        conversaodolar()

    #----------------Busca de CEP
    elif choice == '8':
        limpar()
        cepsearch()

    #----------------Sair do sistema
    elif choice == 's' or choice == 'S' or choice == 'sair' or choice == 'SAIR' or choice == 'Sair':
        limpar()
        loop = 0

    #----------------Opção inválida
    else:
        limpar()
        print(color.RED + "Selecione uma opção válida!" + color.END)
    #------------------------------------------------------------
