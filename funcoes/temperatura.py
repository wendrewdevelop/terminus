import sys
import subprocess 
from configuracoes.configs import color

def timetemperatura():
    print("\n" + color.PURPLE + "para nome composto use 'underline' para separação das palavras" + color.END)
    print(color.PURPLE + "Exemplo: " + color.END + color.BOLD + "sao_paulo" + color.END)
    cidade = input("\nDigite o nome da cidade: \n")
    return_code = subprocess.call('curl wttr.in/' + cidade, shell=True)
    print(return_code)
    