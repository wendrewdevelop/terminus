from configuracoes.configs import color
import random, os, smtplib, random, string, sys, subprocess, time, threading
from googlesearch import search

def google():
    print(color.DARKCYAN + "Pesquisa no google selecionada!\n" + color.END)

    busca = input("Escreva a busca que deseja realizar no motor de busca do google:\n")
    for url in search(busca, stop=20):
        print(url)