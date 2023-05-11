
import tkinter as tk

valor1 = float(input('Digite o valor do produto A:'))
qtd1 = int(input('Digite a quantidade vendida do produto:'))

valor2 =float(input('Digite o valor do produto B:'))
qtd2 = int(input('Digite a quantidade vendida do produto:'))

valor3 = float(input('Digite o valor do produto C:'))
qtd3 = int(input('Digite a quantidade vendida do produto:'))

total = (valor1 * qtd1) + (valor2 * qtd2) + (valor3 * qtd3)

if total >= 500 :
    desconto = total* 0.05
    print(f'Você teve', desconto , ' de desconto!')
    total = total -  desconto
    print(f'Total da sua compra com desconto é:', total)
    
else:
    print(f'O total da compra é de: ', total)




