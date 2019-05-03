from configuracoes.configs import color
import pycep_correios

def cepsearch():
    print(color.CYAN + "Busca por CEP" + color.END)
    
    cep = input("\nDigite o CEP desejado: ")
    endereco = pycep_correios.consultar_cep(cep)
    
    if endereco:
        print(color.BOLD + "Rua: " + color.END, endereco['end'])
        print(color.BOLD + "Bairro: " + color.END, endereco['bairro'])
        print(color.BOLD + "Cidade: " + color.END, endereco['cidade'])
        print(color.BOLD + "Estado: " + color.END, endereco['uf'])
    else:
        print("CEP inválido, tente novamente.")