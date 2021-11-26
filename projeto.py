def main():

    preco = float (input("preco kwH: "))
    numConsumidor = int (input("numero consumidor: "))
    valorPagar = 0
    maiorConsumo = 0
    menorConsumo = 1000
    totalConsumoR = 0
    totalConsumoC = 0
    totalConsumoI = 0
    qtdR = 0
    qtdC = 0
    qtdI = 0
    mediaGeral = 0
    
    while (numConsumidor != 0):
        qtdConsumida = int (input ("qtde consumida: "))
        tipoConsumidor = str (input ("tipo consumidor: "))
        
        if (qtdConsumida > maiorConsumo):
            maiorConsumo = qtdConsumida
        if (qtdConsumida < menorConsumo):
            menorConsumo = qtdConsumida
        if (tipoConsumidor == 'R'):
            totalConsumoR = qtdConsumida + totalConsumoR
            qtdR += 1
        if (tipoConsumidor == 'C'):
            totalConsumoC = qtdConsumida + totalConsumoC
            qtdC += 1
        if (tipoConsumidor == 'I'):
            totalConsumoI = qtdConsumida + totalConsumoI
            qtdI += 1
            
        print (numConsumidor, qtdConsumida * preco)
        numConsumidor = int(input("numero consumidor: "))
    
    print (maiorConsumo)
    print (menorConsumo)
    print (totalConsumoR)
    print (totalConsumoC)
    print (totalConsumoI)
    mediaGeral = (totalConsumoR + totalConsumoC + totalConsumoI) / (qtdR+qtdC+qtdI)
    print (mediaGeral)
    
    return 0

if __name__ == "__main__":
    main()