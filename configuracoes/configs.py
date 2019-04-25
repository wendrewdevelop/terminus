import os

#------------------------------------------------------------
#------------------Configurações globais
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def limpar():
   clear = lambda: os.system('cls') #Windows
   clear = lambda: os.system('clear') #Linux
   clear() #Clear terminal