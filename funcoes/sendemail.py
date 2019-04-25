from configuracoes.configs import color
import random, os, smtplib, random, string, sys, subprocess, time, threading

def email():
    print(color.DARKCYAN + "\nEnvio de e-mail selecionado!\n" + color.END)

    try:
        senders = input(color.BOLD + "Digite o e-mail do remetente: " + color.END)
        receivers = input(color.BOLD + "Digite o e-mail do destinatário: " + color.END)
        msg = input(color.BOLD + "Digite a mensagem do e-mail: " + color.END)

        username = "wendrewdevelop@gmail.com"
        password = "macacolouco"
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(senders,receivers,msg)
        server.quit()

        print(color.GREEN + 'E-mail enviado com sucesso!' + color.END)
    except:  
        print(color.RED + 'Something went wrong...' + color.END)