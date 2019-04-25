from configuracoes.configs import color

def conversaodolar():
    print(color.CYAN + "Conversor de Reais -> Dólar" + color.END)
    dolar = 3.96
    reais = float(input(color.BOLD + "Insira o valor em reais: " + color.END))

    print(color.BOLD + "Reais: R$"  + color.END + color.UNDERLINE, reais, color.END)
    print(color.BOLD + "Dólar: R$"  + color.END + color.UNDERLINE, dolar, color.END)

    result = reais * dolar

    print(color.BOLD + "Valor da conversão é: "+ color.END + color.UNDERLINE, result, color.END)


    