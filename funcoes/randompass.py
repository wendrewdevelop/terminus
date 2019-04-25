from configuracoes.configs import color
import random, os, smtplib, random, string, sys, subprocess, time, threading

def randompass():
    try:
        print(color.DARKCYAN + "Gerando uma senha aleatório (com caracteres especiais)!\n" + color.END)
        def createPass(n):
            allChars = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
            passphrase = []
            for i in range(n):
                tmp = random.choice(allChars)
                passphrase.append(tmp)

            res = "".join(passphrase)
            
            return res

        #realizando testes

        hash5 = createPass(5)# criando uma senha de 5 caracteres
        print(color.BOLD + "Senha com 5 caracteres: " + color.END + hash5)

        hash8 = createPass(8)# criando uma senha de 8 caracteres
        print(color.BOLD + "Senha com 8 caracteres: " + color.END + hash8)
    
        return 
    except:
        print(color.RED + "Deu B.O!" + color.END)

