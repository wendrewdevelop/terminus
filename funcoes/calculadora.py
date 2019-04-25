from configuracoes.configs import color, limpar

def calc():
    # Grupo de funções que realizam os calculos
    def mais(a,b):
        return(a+b)
    def menos(a,b):
        return(a-b)
    def dividir(a,b):
        return(a/b)
    def multiplicar(a,b):
        return(a*b)

    items_calculadora = {
        "S ou Sair": "Sair",
        "1": "Adição",
        "2": "Subtração",
        "3": "Divisão",
        "4": "Multiplicação",
    }

    loop = 1
    escolha = 0
    while loop == 1:
        print(color.YELLOW + "\nCalculadora!\
                            \n=========================================\n" + color.END)
        for names, values in items_calculadora.items():
            print(names, " -> ", values)
        escolha = input(color.BOLD + "\nEscolha uma opção: \n" + color.END)
        escolha = escolha

        if escolha == 's' or escolha == 'S' or escolha == 'sair' or escolha == 'SAIR' or escolha == 'Sair':
            limpar()
            loop = 0
        elif escolha == '1':
            print(color.BOLD + "\nVocê escolheu Adição\n" + color.END)
            n1 = int(input("Insira o primeiro numero: "))
            n2 = int(input("Insira o segundo numero: "))
            print(n1, "+", n2, "=", mais(n1,n2))
        elif escolha == '2':
            print(color.BOLD + "\nVocê escolheu Subtração\n" + color.END)
            n1 = int(input("Insira o primeiro numero: "))
            n2 = int(input("Insira o segundo numero: "))
            print(n1, "-", n2, "=", menos(n1,n2))
        elif escolha == '3':
            print(color.BOLD + "\nVocê escolheu Divisão\n" + color.END)
            n1 = int(input("Insira o primeiro numero: "))
            n2 = int(input("Insira o segundo numero: "))
            print(n1, "/", n2, "=", dividir(n1,n2))
        elif escolha == "4":
            print(color.BOLD + "\nVocê escolheu Multiplicação\n" + color.END)
            n1 = int(input("Insira o primeiro numero: "))
            n2 = int(input("Insira o segundo numero: "))
            print(n1, "*", n2, "=", multiplicar(n1,n2))
        else:
            limpar()
            print(color.RED + "\nSelecione uma opção válida!\n" + color.END)